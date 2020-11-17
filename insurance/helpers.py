from insurance.models import *


def get_workers_by_user(user):
    return OfficeWorkers.objects.filter(office__director=user)


def get_office_list_by_user(user):
    return InsuranceOffice.objects.filter(director=user.id)


def is_user_director_of_office(office_id, user):
    return InsuranceOffice.objects.get(director=user.id, id=office_id) is not None


def is_user_worker_of_director(director, user_id):
    return OfficeWorkers.objects.get(office__director=director, user_id=user_id) is not None
