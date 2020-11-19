from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator


class Position(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name='Тел', max_length=15, null=True, blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='users', null=True, blank=True)
    passport = models.CharField(verbose_name='Паспорт', max_length=50, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    def __str__(self):
        return self.user.username


# signal receiver. when User changed or created, Profile also updated or created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Permission(models.Model):
    code_name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                              related_name='permission_updated_by')
    up_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code_name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userrole_created_by', null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.role.title)


class PermissionRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    grant = models.BooleanField(default=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} {}'.format(self.role.title, self.permission.title, self.grant)


class PermissionUser(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grant = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permissionuser_created_by', null=True,
                              blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.permission.__str__() + ' ' + self.user.__str__()


class Group(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductTypeClass(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vid(models.Model):
    name = models.CharField(max_length=256)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PolicySeriesType(models.Model):
    code = models.CharField(verbose_name="Код", max_length=24)

    cr_on = models.DateTimeField(auto_now_add=True)

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_series_cr_by')

    class Meta:
        verbose_name = "Серии полиса"
        verbose_name_plural = 'Серии полисов'

    def __str__(self):
        return self.code


class PoliciesIncome(models.Model):
    act_number = models.CharField(verbose_name="Номер акта", max_length=128, unique=True)
    act_date = models.DateTimeField(verbose_name="Дата акта")

    policy_series = models.ForeignKey(PolicySeriesType,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True, default=None,
                                      verbose_name="Серии полиса")

    policy_number_from = models.PositiveIntegerField(verbose_name="Номер полиса с", default=1)
    policy_number_to = models.PositiveIntegerField(verbose_name="Номер полиса до", default=2)
    is_free_policy = models.BooleanField(verbose_name="Свободный", default=False)

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name="policies_income_up_by")

    document = models.FileField(verbose_name="Документ", upload_to='policies_income', blank=True, null=True,
                                default=None)

    cr_on = models.DateTimeField(auto_now_add=True)

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policies_income_cr_by')

    class Meta:
        verbose_name = 'Поступления полис'
        verbose_name_plural = 'Поступления полисы'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.act_number + " " + self.cr_by.__str__()


class ProductType(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    klass = models.ForeignKey(ProductTypeClass, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    vid = models.ForeignKey(Vid, on_delete=models.CASCADE, null=True)
    is_exist = models.BooleanField(default=True)


class Human(models.Model):
    phone = models.CharField(verbose_name="Номер телефона", max_length=14, default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=128, default=None)
    last_name = models.CharField(verbose_name="Фамилия", max_length=128, default=None)
    middle_name = models.CharField(verbose_name="Отчество", max_length=128, default=None)
    address = models.CharField(verbose_name="Адрес", max_length=1024, default=None)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Bank(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=128, default=None)
    mfo = models.CharField(max_length=6, null=True)
    inn = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=14, default=None)
    address = models.CharField(verbose_name="Адрес", max_length=1024, default=None)
    checking_account = models.CharField(verbose_name="Расчётный счёт", max_length=30)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.name, self.mfo)


class LocationType(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Location(models.Model):
    series = models.CharField(max_length=10, default=None, blank=False)
    name = models.CharField(max_length=512)
    type = models.ForeignKey(LocationType, on_delete=models.SET_NULL, blank=False, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.series} - {self.name}'


class OfficeType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=1024)
    description = models.CharField(verbose_name='Описание', max_length=2048)

    def __str__(self):
        return self.title


class InsuranceOffice(models.Model):
    series = models.CharField(verbose_name="Серии", max_length=10, default="AAA")

    name = models.CharField(verbose_name="Наименование", max_length=255)

    director = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='insurance_director')

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    office_type = models.ForeignKey(OfficeType, on_delete=models.SET_NULL, null=True, blank=True)

    location = models.CharField(verbose_name="Местонахождение", max_length=1024, default='')

    region = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    founded_date = models.DateField(verbose_name="Основан", blank=False, null=True)

    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='office_cr_by')
    up_on = models.DateTimeField(auto_now=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='office_up_by')
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OfficeWorkers(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='office_workers_user')
    office = models.ForeignKey(InsuranceOffice, on_delete=models.DO_NOTHING, related_name='office_workers_office')
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='office_workers_cr_by')
    up_on = models.DateTimeField(auto_now=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='office_workers_up_by')

    def __str__(self):
        return self.user.username + ' works at ' + self.office.name


class Currency(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=50)
    code = models.CharField(verbose_name="Код валюты", max_length=4, unique=True)
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.code


class BasicTariffRate(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    sum = models.BigIntegerField(verbose_name="Сумма")


class Beneficiary(models.Model):
    person = models.ForeignKey(Human, on_delete=models.SET_NULL, null=True)
    fax_number = models.CharField(max_length=64, null=True)
    checking_account = models.CharField(max_length=64, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, related_name='beneficiary_bank', null=True)
    inn = models.CharField(max_length=20, null=True)
    mfo = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.person.__str__() + ' ' + self.inn


class LegalClient(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    address = models.CharField(verbose_name="Адрес", max_length=150)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='legal_client_up_by')
    up_on = models.DateTimeField(auto_now_add=True)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class IndividualClient(models.Model):
    person = models.ForeignKey(Human, on_delete=models.SET_NULL, null=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='individual_client_up_by')
    up_on = models.DateTimeField(auto_now_add=True)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.person.first_name, self.person.last_name)


class Pledger(models.Model):
    person = models.ForeignKey(Human, on_delete=models.SET_NULL, null=True, default=None)
    fax_number = models.CharField(max_length=32)
    checking_account = models.CharField(max_length=32)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True)
    inn = models.CharField(max_length=20, null=True)
    mfo = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.person.__str__()


class Policy(models.Model):
    series = models.ForeignKey(PolicySeriesType, on_delete=models.SET_NULL, null=True, blank=True)
    is_free_generated = models.BooleanField(default=False, verbose_name="Свободный")
    policy_number = models.PositiveIntegerField(verbose_name="Номер")

    product = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    client_type = models.CharField(max_length=64, null=True, blank=True, default=None)

    date_from = models.DateField(null=True, blank=True, default=None)

    date_to = models.DateField(null=True, blank=True, default=None)

    goal = models.CharField(max_length=2048, null=True, blank=True, default=None)

    zone = models.CharField(max_length=256, null=True, blank=True, default=None)

    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    pledger = models.ForeignKey(Pledger, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    income_session = models.ForeignKey(PoliciesIncome, verbose_name="Policies income session",
                                       on_delete=models.SET_NULL,
                                       default=None, null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name="Active", null=False, blank=False)

    def __str__(self):
        return self.series.__str__() + '|' + self.policy_number.__str__()


class PolicyTransfers(models.Model):
    to_office = models.ForeignKey(InsuranceOffice, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name='policy_transfer_to_office')
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_transfers_cr_by')

    def __str__(self):
        return self.to_office.__str__()


class PolicyRetransfer(models.Model):
    transfer = models.ForeignKey(PolicyTransfers, on_delete=models.DO_NOTHING, null=False, blank=False,
                                 related_name='policy_retransfer_transfer_parent')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_retransfer_cr_by')

    def __str__(self):
        return self.transfer.__str__()


class Dt_Option(models.Model):
    codeName = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    dataPath = models.CharField(max_length=512, null=True, blank=True)
    draw = models.IntegerField(default=1, null=True, blank=True)
    keys = models.BooleanField(default=True)
    colReorder = models.BooleanField(default=True)
    fixedHeader = models.BooleanField(default=True)
    responsive = models.BooleanField(default=True)
    autoFill = models.BooleanField(default=True)
    serverSide = models.BooleanField(default=True)
    processing = models.BooleanField(default=True)
    scrollY = models.CharField(max_length=128, default='70vh')

    def __str__(self):
        return self.codeName


class GridCols(models.Model):
    table = models.ForeignKey(Dt_Option, on_delete=models.CASCADE, related_name='columns', null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    data = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    type = models.CharField(max_length=128, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    searchable = models.BooleanField(default=True)
    orderable = models.BooleanField(default=True)
    className = models.CharField(max_length=128, null=True, blank=True)
    defaultContent = models.CharField(max_length=1024, null=True, blank=True)
    visible = models.BooleanField(default=True)
    order_num = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['order_num']

    def __str__(self):
        return self.title


class ProductField(models.Model):
    product = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=4096)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Insurer(models.Model):
    person = models.ForeignKey(Human, on_delete=models.SET_NULL, null=True)
    fax_number = models.CharField(max_length=32)
    checking_account = models.CharField(max_length=32)
    bank_name = models.CharField(max_length=256, null=True)
    inn = models.CharField(max_length=20, null=True)
    mfo = models.CharField(max_length=6, null=True)

    def __str__(self):
        return "{} ".format(self.person)


class PolicyFields(models.Model):
    product = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=128, null=True)
    value = models.CharField(max_length=4096, null=True, blank=True)

    def __str__(self):
        return self.name


class ClientRequestType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=1024)
    description = models.CharField(verbose_name='Описание', max_length=2048)

    def __str__(self):
        return self.title


class ClientRequest(models.Model):
    request_type = models.ForeignKey(ClientRequestType, verbose_name='Тип запроса', on_delete=models.SET_NULL, null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=False, blank=False)
    policy_series = models.CharField(max_length=100, null=False, blank=False)
    reason = models.CharField(verbose_name='Причина увеличения лимитов', max_length=4000)
    file = models.FileField(verbose_name="Документ", upload_to='client_requests', blank=True, null=True, default=None)
    comment = models.CharField(verbose_name='Комментарий', max_length=4000)

    is_approved = models.BooleanField(verbose_name='Одобрено', default=False)

    assigned_to = models.ForeignKey(User, verbose_name='Назначен', on_delete=models.SET_NULL, default=None, null=True,
                                    blank=True)

    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                              related_name='client_request_updated_by')
    up_on = models.DateTimeField(auto_now_add=True)
