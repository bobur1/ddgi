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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name='Тел', max_length=15, null=True, blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='users', null=True, blank=True)
    passport = models.CharField(verbose_name='Паспорт', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username


#### signal receiver. when User changed or created, Profile also updated or created
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


class Role(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


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


class ClientPhysical(models.Model):
    firstname = models.CharField(verbose_name="Имя", max_length=50)
    lastname = models.CharField(verbose_name="Фамилия", max_length=50)
    middlename = models.CharField(verbose_name="Отчество", max_length=50)


class Group(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Klass(models.Model):
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

    document = models.FileField(verbose_name="Документ", upload_to='policies_income', blank=True, null=True, default=None)

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
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, null=True)
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


class Branch(models.Model):
    series = models.CharField(verbose_name="Серии", max_length=10, default="AAA")
    name = models.CharField(verbose_name="Наименование", max_length=255)
    director = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='branch_director')
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='branch_cr_by')
    up_on = models.DateTimeField(auto_now=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='branch_up_by')
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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


class InsurancePeriod(models.Model):
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)


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


#
# class CompanyBankAccount(models.Model):
#     bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True)
#     name = models.CharField(verbose_name="Наименование", max_length=255)
#     address = models.CharField(verbose_name="Адрес", max_length=150)
#     phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)
#     checking_account = models.CharField(verbose_name="Расчётный счёт", max_length=30)
#
#
# class InsuranceContract(models.Model):
#     contract_number = models.IntegerField(verbose_name="Номер договора")  # TODO: make unsigned
#     contract_date = models.DateTimeField(verbose_name="Дата договора")  # TODO: discuss
#     # region = models.ForeignKey(Region, on_delete=models.SET_NULL)  TODO: fix
#     client_id = models.BigIntegerField()    # TODO: make unsigned
#     client_type = models.CharField(verbose_name="Тип клиента", max_length=1)
#     # client_checking_account = models.CharField(verbose_name="Расчётный счёт клиента", max_length=30)  TODO: discuss
#     # beneficiary = models.ForeignKey(Beneficiary, verbose_name="Выгодоприобретатель", on_delete=models.SET_NULL)  TODO: discuss
#     # pledger = models.ForeignKey(Pledger, verbose_name="Залогодатель", on_delete=models.SET_NULL)  TODO: discuss
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     loan_agreement = models.CharField(verbose_name="Кредитный договор", max_length=150)
#     property_name = models.CharField(verbose_name="Имя имущества", max_length=100)
#     quantity = models.IntegerField(verbose_name="Количество")  # TODO: discuss
#     insurance_cost = models.BigIntegerField(verbose_name="Страховая стоимость")  # TODO: discuss
#     insurance_sum = models.BigIntegerField(verbose_name="Страховая сумма")  # TODO: discuss
#     date_from = models.DateField()
#     date_to = models.DateField(null=True, blank=True)
#     franchise = models.CharField(verbose_name="Франшиза", max_length=100)
#     # installment_date = models.SmallIntegerField(verbose_name="Дата взносов")  TODO: discuss
#     original = models.TextField()  # TODO: change to Jsonb field
#
#

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

    def __str__(self):
        return self.series.__str__() + '|' + self.policy_number.__str__()

# class Policy(models.Model):
#     contract = models.ForeignKey(InsuranceContract, on_delete=models.SET_NULL, null=True, blank=True)
#     contract_number = models.IntegerField(verbose_name="Номер договора")  # TODO: make unsigned
#     property_name = models.CharField(verbose_name="Имя имущества", max_length=100)
#     # insurance_place = models.ForeignKey(Region, on_delete=models.SET_NULL)  TODO: fix
#     loan_agreement = models.CharField(verbose_name="Кредитный договор", max_length=150)
#     quantity = models.IntegerField(verbose_name="Количество")  # TODO: discuss
#     insurance_case = models.CharField(verbose_name="Страховой случае", max_length=100)
#     insurance_sum = models.BigIntegerField(verbose_name="Страховая сумма")  # TODO: discuss
#     franchise = models.CharField(verbose_name="Франшиза", max_length=100)
#     total_prize = models.BigIntegerField(verbose_name=" Общая страховая премия")  # TODO: discuss
#     paid_insurance_prize = models.BigIntegerField(verbose_name="Оплаченная страховая премия")  # TODO: discuss
#     date_from = models.DateField()
#     date_to = models.DateField(null=True, blank=True)
#     policy_date = models.DateField(verbose_name="Дата полиса")
#     issue_date = models.DateField(verbose_name="Дата выдачи")
#     # manager = models.ForeignKey(Beneficiary, verbose_name="Директор", on_delete=models.SET_NULL)  TODO: discuss
#     original = models.TextField()  # TODO: change to Jsonb field


class PolicyTransfers(models.Model):
    to_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    policies = models.ManyToManyField(Policy)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_transfers_cr_by')


# class PolicyReTransfer(models.Model):
#     parent_transfer = models.ForeignKey(PolicyTransfers, verbose_name="Перевод", on_delete=models.DEFERRED, null=False, blank=False)
#     act_date = models.CharField(verbose_name="Дата акта", max_length=128)
#     policy_number_from = models.PositiveIntegerField(verbose_name="Номер полиса с",
#                                                      validators=[MinValueValidator(parent_transfer.policy_number_from),
#                                                                  MaxValueValidator(parent_transfer.policy_number_to)])
#     policy_number_to = models.PositiveIntegerField(verbose_name="Номер полиса до")


class RegisteredPolises(models.Model):
    act_number = models.CharField(verbose_name="Номер акта", max_length=128)
    act_date = models.CharField(verbose_name="Дата акта", max_length=128)
    polis_number_from = models.IntegerField(verbose_name="Номер полиса с")
    polis_number_to = models.IntegerField(verbose_name="Номер полиса до")
    polis_quantity = models.IntegerField(verbose_name="Количество полисво")
    polis_status = models.SmallIntegerField(verbose_name="Статус полиса")
    document = models.FileField(verbose_name="Документ", upload_to='registered_polis')
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='polise_register_up_by')
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Зарегистрированные полисы'
        verbose_name = 'зарегистрированный полис'

    def __str__(self):
        return '{} {}'.format(self.act_number, self.act_date)


#
#
# class Transaction(models.Model):
#     client_id = models.BigIntegerField()    # TODO: make unsigned
#     client_type = models.CharField(verbose_name="Тип клиента", max_length=1)
#     bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True)
#     sum = models.BigIntegerField(verbose_name="Сумма")
#     time = models.DateField(auto_now_add=True)
#     bank_checking_account = models.ForeignKey(CompanyBankAccount, verbose_name="Расчётный счёт", on_delete=models.SET_NULL, null=True, blank=True)
#     client_checking_account = models.CharField(verbose_name="Расчётный счёт клиента", max_length=30)
#     contract = models.ForeignKey(InsuranceContract, on_delete=models.SET_NULL, null=True, blank=True)
#     comments = models.TextField()   # TODO: discuss about jsonb
#
#
# class Form(models.Model):
#     # beneficiary = models.ForeignKey(Beneficiary, verbose_name="Выгодоприобретатель", on_delete=models.SET_NULL)  TODO: discuss
#     # form_type = models.ForeignKey(FormType)
#     date_from = models.DateField()
#     date_to = models.DateField(null=True, blank=True)
#     property_name = models.CharField(verbose_name="Имя имущества", max_length=100)
#     client_id = models.BigIntegerField()    # TODO: make unsigned
#     client_type = models.CharField(verbose_name="Тип клиента", max_length=1)
#     # client_checking_account = models.CharField(verbose_name="Расчётный счёт клиента", max_length=30)  TODO: discuss
#     # region = models.ForeignKey(Region, on_delete=models.SET_NULL)  TODO: fix
#     quantity = models.IntegerField(verbose_name="Количество")  # TODO: discuss
#     insurance_cost = models.BigIntegerField(verbose_name="Страховая стоимость")  # TODO: discuss
#     insurance_sum = models.BigIntegerField(verbose_name="Страховая сумма")  # TODO: discuss
#     anti_fire_stuff = models.SmallIntegerField(verbose_name="Наличие пожарной сигнализации и средств пожаротушения")
#     security_stuff = models.SmallIntegerField(verbose_name="Наличие охранной сигнализации и средств защиты")
#     payment_type = models.CharField(verbose_name="Вид оплаты", max_length=1)
#     payment_currency = models.CharField(verbose_name="Валюта оплаты", max_length=4)
#     insurer = models.ForeignKey(User, verbose_name="Страхователь", on_delete=models.SET_NULL, null=True, blank=True)


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


class Region(models.Model):
    name = models.CharField(max_length=512)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    is_exist = models.BooleanField(default=True)

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
