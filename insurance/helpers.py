from datetime import datetime
from rest_framework.response import Response
from insurance.models import *


def get_workers_by_user(user_id):
    return OfficeWorkers.objects.filter(office__director_id=user_id)


def get_workers_by_office(office_id):
    return OfficeWorkers.objects.filter(office_id=office_id)


def get_office_list_by_user(user):
    return InsuranceOffice.objects.filter(director=user.id)


def is_user_director_of_office(office_id, user):
    return InsuranceOffice.objects.get(director=user.id, id=office_id) is not None


def is_user_worker_of_director(director, user_id):
    return OfficeWorkers.objects.get(office__director=director, user_id=user_id) is not None


def get_all_policies():
    return Policy.objects.all()


def get_all_active_policies():
    return Policy.objects.filter(is_active=True)


def is_valid_policies_range(is_freely_generated, series, from_number, to_number):
    s_id = 'NULL'
    if series != '' and series is not None:
        s_id = int(series)
    query = 'SELECT * FROM insurance_policy where series_id is {} AND policy_number>={}'.format(s_id, from_number)
    objs = Policy.objects.raw(raw_query=query)
    result = objs.__len__() == 0
    return result


def generate_policies(from_number, to_number, is_free_generated, series, session):
    for i in range(int(from_number), int(to_number) + 1):
        s = None
        if series != '' and series is not None:
            s = PolicySeriesType.objects.get(id=series)

        Policy.objects.create(policy_number=i,
                              series=s,
                              is_free_generated=is_free_generated,
                              is_active=True,
                              income_session=session).save()


def create_insurance_office(series, name, director, parent, office_type, location, region, funded, created_by, bank_ids,
                            phone_number):
    banks = Bank.objects.filter(id__in=bank_ids)

    office = InsuranceOffice.objects.create(series=series, name=name, director=director, parent=parent,
                                            location=location, region=region,
                                            office_type=office_type,
                                            founded_date=funded, cr_on=datetime.now(), cr_by=created_by,
                                            is_exist=True,
                                            contact=phone_number)
    for b in banks:
        office.bank.add(b)
    office.save()


def edit_insurance_office(office_id, series, name, director, parent, office_type,
                          location, region, funded, created_by, bank_ids, is_exist,
                          phone_number):
    banks = Bank.objects.filter(id__in=bank_ids)

    office = InsuranceOffice.objects.get(id=office_id)

    office.series = series
    office.name = name
    office.director = director
    office.parent = parent
    office.location = location
    office.region = region
    office.office_type = office_type
    office.founded_date = funded
    office.contact = phone_number
    office.is_exists = is_exist
    office.up_by = created_by
    office.up_on = datetime.now()

    for b in banks:
        office.bank.add(b)
    office.save()


def create_update_product_type(request):
    type_id = request.data.get('id', None)
    code = request.data.get('code')
    name = request.data.get('name')
    client_type = request.data.get('client_type')

    product_type_codes = request.data.get('product_code_types', [])

    type_codes = ProductTypeCode.objects.filter(id__in=product_type_codes)

    has_beneficiary = request.data.get('has_beneficiary', False)
    has_pledger = request.data.get('has_pledger', False)
    min_acceptable_amount = request.data.get('min_acceptable_amount')
    max_acceptable_amount = request.data.get('max_acceptable_amount')
    is_exist = request.data.get('is_active', True)

    if type_id is None:
        product = ProductType.objects.create(code=code,
                                             name=name,
                                             client_type=client_type,
                                             has_beneficiary=has_beneficiary,
                                             has_pledger=has_pledger,
                                             min_acceptable_amount=min_acceptable_amount,
                                             max_acceptable_amount=max_acceptable_amount)
        product.classes.set(type_codes)

        product.save()
    else:
        product = ProductType.objects.get(id=type_id)
        product.code = code
        product.name = name
        product.client_type = client_type
        product.classes = product_type_codes
        product.has_beneficiary = has_beneficiary
        product.has_pledger = has_pledger
        product.min_acceptable_amount = min_acceptable_amount
        product.max_acceptable_amount = max_acceptable_amount
        product.is_exist = is_exist
        product.save()


def create_update_product_type_code(request):
    code_id = request.data.get('id', None)
    code = request.data.get('code')
    name = request.data.get('name')
    description = request.data.get('description')
    is_active = request.data.get('is_active', True)
    obj, created = ProductTypeCode.objects.update_or_create(id=code_id, defaults={'code': code, 'name': name,
                                                                                  'description': description,
                                                                                  'is_exist': is_active})
    print(f'created {created}')


def create_update_office_worker(request):
    worker_id = request.data.get('worker_id', None)

    if worker_id is not None:
        worker = OfficeWorkers.objects.get(id=worker_id)
        office_id = request.data.get('office_id', None) or worker.office_id
        worker.office_id = office_id
        worker.up_by = request.user
        worker.up_on = datetime.now()
        worker.save()
    else:
        #create
        office_id = request.data.get('office_id')
        user_id = request.data.get('user_id')

        OfficeWorkers.objects.create(user_id=user_id, office_id=office_id, cr_by=request.user,
                                     cr_on=datetime.now())


def create_update_region(request):
    response = {}
    region_id = request.data.get('region_id')
    series = request.data.get('series', None)
    name = request.data.get('name', None)
    type_id = request.data.get('type_id', None)
    try:
        if region_id is not None:
            region = Location.objects.get(id = region_id)
            region.series = series or region.series
            region.name = name or region.name
            region.type_id = type_id or region.type_id
            region.save()
        else:
            Location.objects.create(series=series, name=name, type_id=type_id)

        response['success'] = True

    except Exception as e:
        response['success'] = False
        response['error_msg'] = e.__str__()

    return Response(response)


def get_transferred_policies_by(user):
    retransferred_policies = PolicyRetransfer.objects.filter(to_user=user)
    policies = []
    for rtf in retransferred_policies:
        policies.append(rtf.transfer.policy)

    return policies


def create_update_region_type(request):
    type_id = request.data.get('type_id', None)
    name = request.data.get('name', None)
    details = request.data.get('details', None)
    response = {}
    try:
        if type_id is not None:
            obj = LocationType.objects.get(id=type_id)
            obj.name = name or obj.name
            obj.description = details or obj.description
            obj.save()
        else:
            LocationType.objects.create(name=name, description=details)
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = e.__str__()

    return Response(response)


def create_update_legal_client(request):
    client_id = request.data.get('client_id', None)
    name = request.data.get('name', None)
    address = request.data.get('address', None)
    phone_number = request.data.get('phone_number', None)
    inn = request.data.get('inn', None)
    bank_id = request.data.get('bank_id', None)
    is_exists = request.data.get('is_exists', None)
    okohx = request.data.get('okohx', None)

    cr_by = request.user
    up_by = request.user
    cr_on = datetime.now()
    up_on = datetime.now()

    if client_id is not None:
        obj = LegalClient.objects.get(id=client_id)
        obj.name = name or obj.name
        obj.address = address or obj.address
        obj.phone_number = phone_number or obj.phone_number
        obj.inn = inn or obj.inn
        obj.bank_id = bank_id or obj.bank_id
        obj.is_exist = is_exists or obj.is_exist
        obj.up_by = up_by
        obj.up_on = up_on
        obj.okohx = okohx or obj.okohx
        obj.save()
    else:
        LegalClient.objects.create(
            name=name,
            address=address,
            phone_number=phone_number,
            inn=inn,
            bank_id=bank_id,
            is_exists=is_exists or True,
            cr_by=cr_by,
            cr_on=cr_on,
            okohx=okohx
        ).save()


def create_update_individual_client(request):

    client_id = request.data.get('client_id', None)
    phone = request.data.get('phone', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    middle_name = request.data.get('middle_name', None)
    address = request.data.get('address', None)
    p_series = request.data.get('passport_series', None)
    p_number = request.data.get('passport_number', None)
    p_given_date = request.data.get('passport_given_date', None)
    p_given_by = request.data.get('passport_given_by', None)
    bank_id = request.data.get('bank_id', None)
    inn = request.data.get('inn', None)
    cr_by = request.user
    cr_on = datetime.now()

    up_by = request.user
    up_on = datetime.now()
    is_exists = request.data.get('is_exists', None)

    if client_id is not None:
        obj = IndividualClient.objects.get(id=client_id)
        obj.phone = phone or obj.phone
        obj.first_name = first_name or obj.first_name
        obj.last_name = last_name or obj.last_name
        obj.middle_name = middle_name or obj.middle_name
        obj.address = address or obj.address
        obj.passport_series = p_series or obj.passport_series
        obj.passport_number = p_number or obj.passport_number
        obj.passport_given_date = p_given_date or obj.passport_given_date
        obj.passport_given_by = p_given_by or obj.passport_given_by
        obj.bank_id = bank_id or obj.bank_id
        obj.inn = inn or obj.inn
        obj.is_exist = is_exists or obj.is_exist
        obj.up_by = up_by
        obj.up_on = up_on
        obj.save()
    else:
        IndividualClient.objects.create(
            phone=phone or "",
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            address=address,
            passport_series=p_series,
            passport_number=p_number,
            passport_given_date=p_given_date,
            passport_given_by=p_given_by,
            bank_id=bank_id,
            inn=inn,
            cr_by=cr_by,
            cr_on=cr_on,
            is_exist=is_exists or True
        )
