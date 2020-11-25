from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from insurance import util
from insurance.models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['userdata'] = util.get_user_profile(self.user)
        data['roles'] = util.get_user_roles(self.user)
        data['permissions'] = util.get_user_permissions(self.user)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserRoleSerializer(serializers.ModelSerializer):
    role_title = serializers.CharField(source="role.title")

    class Meta:
        model = UserRole
        fields = ('role_title',)


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class PoliciesIncomeSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()

    class Meta:
        model = PoliciesIncome
        fields = ['act_number', 'act_date', 'policy_number_from', 'policy_number_to',
                  'is_free_policy', 'from_user', 'document']


class ClassifiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypeCode
        fields = ['id', 'code', 'name', 'description', 'is_exist']


class ProductFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        fields = ['id', 'product', 'input_type', 'name', 'value', 'order']


class ProductSerializer(serializers.ModelSerializer):
    classes = ClassifiersSerializer(many=True)

    class Meta:
        model = ProductType
        fields = ['id', 'code', 'name', 'classes', 'client_type', 'has_beneficiary', 'has_pledger',
                  'min_acceptable_amount', 'max_acceptable_amount']


class PoliciesSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    income_session = PoliciesIncomeSerializer()

    class Meta:
        model = Policy
        fields = ['id', 'series', 'is_free_generated', 'policy_number', 'product', 'client_type',
                  'date_from', 'date_to', 'goal', 'zone', 'beneficiary', 'pledger', 'income_session']


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.CharField(source="user.email")
    position_name = serializers.CharField(source="position")
    is_active = serializers.BooleanField(source="user.is_active")
    is_superuser = serializers.BooleanField(source="user.is_superuser")
    last_login = serializers.DateTimeField(source="user.last_login", format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = Profile
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'position_name',
                  'middle_name',
                  'is_active',
                  'is_superuser',
                  'last_login')


class UserDetailedSerializer(serializers.ModelSerializer):
    class InnerProfileSerializer(serializers.ModelSerializer):
        position_name = serializers.CharField(source="position")
        last_login = serializers.DateTimeField(source="user.last_login", format="%d.%m.%Y %H:%M:%S")
        is_active = serializers.BooleanField(source="user.is_active")

        class Meta:
            model = Profile
            fields = ('id', 'position_name', 'middle_name', 'last_login', 'is_active')

    profile = InnerProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile')


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionUserSerializer(serializers.ModelSerializer):
    permission_code = serializers.CharField(source="permission.code_name")

    class Meta:
        model = PermissionUser
        fields = ('permission_code', 'grant')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'is_active')


class GridColSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridCols
        fields = ['title',
                  'data',
                  'name',
                  'type',
                  'width',
                  'searchable',
                  'orderable',
                  'className',
                  'defaultContent',
                  'visible']


class DtOptionSerializer(serializers.ModelSerializer):
    columns = GridColSerializer(many=True, read_only=True)

    class Meta:
        model = Dt_Option
        fields = ['codeName', 'title', 'dataPath', 'draw',
                  'keys', 'colReorder', 'fixedHeader', 'responsive',
                  'autoFill', 'serverSide', 'processing', 'scrollY', 'columns']


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'phone']


class IndividualClientSerializer(serializers.ModelSerializer):
    # person = HumanSerializer()
    person_first_name = serializers.CharField(source='person.first_name')

    class Meta:
        model = IndividualClient
        fields = ['id', 'person_first_name']


class LegalClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalClient
        fields = ['id', 'name', 'address', 'phone_number',
                  'fax_number', 'checking_account', 'bank_name', 'inn', 'mfo']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'code']


class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypeCode
        fields = ['id', 'name']


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'branch_name', 'mfo', 'inn',
                  'address', 'phone_number', 'checking_account']


class BranchSerializer(serializers.ModelSerializer):
    director = UserDetailedSerializer()

    class Meta:
        model = InsuranceOffice
        fields = ['id', 'name', 'is_branch', 'director']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'type', 'is_active']


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ['id', 'first_name', 'last_name', 'middle_name',
                  'address', 'fax_number', 'checking_number',
                  'bank_name', 'inn', 'mfo']


class Insurer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'address',
                  'phone_number', 'fax_number', 'checking_account', 'bank_name', 'inn', 'mfo']


class ActSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['id', 'client_type', 'date_from', 'date_to',
                  'insurance', 'goal', 'zone', 'is_damaged',
                  'is_insured', 'risk']


class ActFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyFields
        fields = ['id', 'product', 'order', 'name', 'value']


class PolicySeriesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicySeriesType
        fields = ['id', 'code']


class PoliciesSimpleSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    # income_session = PoliciesIncomeSerializer()

    class Meta:
        model = Policy
        fields = ['series', 'is_free_generated', 'policy_number', 'product', 'client_type',
                  'date_from', 'date_to', 'goal', 'zone', 'beneficiary', 'pledger']


class TransferPoliciesSerializer(serializers.ModelSerializer):
    policy = PoliciesSimpleSerializer()

    class Meta:
        model = PolicyTransfers
        fields = ['id', 'to_office', 'policy', 'cr_by', 'cr_on']


class RetransferPoliciesSerializer(serializers.ModelSerializer):
    to_user = UserSerializer()
    transfer = TransferPoliciesSerializer()

    class Meta:
        model = PolicyRetransfer
        fields = ['id', 'transfer', 'to_user', 'cr_by', 'cr_on']


class OfficeWorkersSerializer(serializers.ModelSerializer):
    user = UserDetailedSerializer()
    office = BranchSerializer()

    class Meta:
        model = OfficeWorkers
        fields = ['id', 'user', 'office', 'cr_on']


class ProductTypeCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypeCode
        fields = ['code', 'name', 'description', 'is_exist']
