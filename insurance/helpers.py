from datetime import datetime

from insurance.models import *


def get_workers_by_user(user):
    return OfficeWorkers.objects.filter(office__director=user)


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
                                             # classes=type_codes,
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
        #update
        user = User.objects.get(id=request.data.get('worker_user_id', None))
        worker = OfficeWorkers.objects.get(id=worker_id)
        worker.user
    else:
        #create
        OfficeWorkers.objects.create()

def get_transferred_policies_by(user):
    retransferred_policies = PolicyRetransfer.objects.filter(to_user=user)
    policies = []
    for rtf in retransferred_policies:
        policies.append(rtf.transfer.policy)

    return policies
