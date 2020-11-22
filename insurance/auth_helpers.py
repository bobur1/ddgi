from datetime import datetime

from insurance.models import *


def is_user_exists(login):
    return User.objects.exists(username__in=login)


def is_free_login(login):
    return is_user_exists(login=login) is False


def create_user(login, email, password, is_active, first_name=None, last_name=None):
    user = User.objects.create(username=login, email=email, is_superuser=False, is_active=is_active, is_staff=True)
    user.set_password(password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    # user.profile.middle_name =
    return user


def register_user_profile(user, position, middle_name, phone_number, passport_number, passport_series, created_by,
                          document, image=None):
    try:

        user.profile.middle_name = middle_name
        user.profile.position = position
        user.profile.phone = phone_number
        user.profile.passport_series = passport_series
        user.profile.passport_number = passport_number
        user.profile.created_by = created_by
        user.profile.document = document
        user.profile.image = image
        user.save()
        return True
    except:
        return False


def edit_profile(request):
    user_id = request.data.get('user_id', None)
    user = User.objects.get(id=user_id)

    profile = user.profile

    email = request.data.get('email', user.email)
    password = request.data.get('password', None)
    phone_number = request.data.get('phone_number', user.profile.phone)
    status = request.data.get('is_active', user.profile.is_active)
    position = Position.objects.get(id=request.data.get('position_id', user.profile.position.id))
    first_name = request.data.get('first_name', user.first_name)
    last_name = request.data.get('last_name', user.last_name)
    middle_name = request.data.get('middle_name', profile.middle_name)
    passport_number = request.data.get('passport_number', profile.passport_number.__str__())
    passport_series = request.data.get('passport_series', profile.passport_series)
    document = request.FILES.get('file', None)
    image = request.FILES.get('image', None)
    if document is None:
        document = user.profile.document
    updated_by = request.user

    if password is not None:
        user.set_password(password)

    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = status

    if user is not None:
        profile.position = position
        profile.image = image
        profile.middle_name = middle_name
        profile.phone = phone_number
        profile.passport_number = passport_number
        profile.passport_series = passport_series
        profile.updated_by = updated_by
        profile.document = document
        profile.image = None

    user.save()
