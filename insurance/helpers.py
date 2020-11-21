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
    banks = Bank.objects.filter(id in bank_ids)

    InsuranceOffice.objects.create(series=series, name=name, director=director, parent=parent,
                                   location=location, region=region,
                                   office_type=office_type,
                                   founded_date=funded, cr_on=datetime.now(), cr_by=created_by,
                                   is_exist=True,
                                   banks=banks,
                                   contact=phone_number)


def edit_insurance_office(office_id, series, name, director, parent, office_type, location, region, funded, created_by,
                          bank_ids,
                          phone_number):
    banks = Bank.objects.filter(id in bank_ids)

    InsuranceOffice.objects.update_or_create(id=office_id, series=series, name=name, director=director, parent=parent,
                                             location=location, region=region,
                                             office_type=office_type,
                                             founded_date=funded, cr_on=datetime.now(), cr_by=created_by,
                                             is_exist=True,
                                             banks=banks,
                                             contact=phone_number)
