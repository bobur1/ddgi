from insurance.helpers import *
from insurance.auth_helpers import *

from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from insurance.serializers import *
from insurance.serializers import ActSerializer
from django.core.paginator import Paginator
from rest_framework import viewsets
import json
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def test_view(request):
    response = {'success': True, 'authenticated_user': request.user.username}
    return Response(response)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def product_fields(request):
    serializer = ProductFieldsSerializer(ProductField.objects.all(), many=True)
    response = {
        'data': serializer.data,
        'success': True
    }

    return JsonResponse(response)


def policy_series(request):
    serializer = PolicySeriesTypeSerializer(PolicySeriesType.objects.all(), many=True)
    response = {
        'data': serializer.data,
        'success': True
    }

    return JsonResponse(response)


@api_view(['POST'])
def deactivate_policy(request):
    response = {}
    try:
        policy_id = request.data.get('policy_id', None)
        policy = Policy.objects.get(id=policy_id)
        policy.is_active = False
        policy.save()
        response['success'] = True
    except Exception as e:
        response['error_msg'] = e.__str__()
        response['success'] = False
    return JsonResponse(response)


@api_view(['POST'])
def create_update_office(request):
    response = {}
    try:
        reason = request.data.get('reason', 1)

        office_id = request.data.get('office_id', None)
        series = request.data.get('series')
        director_id = request.data.get('director_id')
        director = User.objects.get(id=director_id)
        created_by = request.user
        office_type = OfficeType.objects.get(id=request.data.get('office_type'))
        bank_ids = request.data.get('bank_ids', [])
        contact = request.data.get('phone_number', None)
        parent_id = request.data.get('parent_id', None)

        parent = None
        if parent_id is not None:
            parent = InsuranceOffice.objects.get(id=parent_id)

        name = request.data.get('title')
        address = request.data.get('address')
        founded_date = request.data.get('founded_date')

        if founded_date is None:
            founded_date = datetime.now().date()
        region = Location.objects.get(id=request.data.get('region_id'))

        if reason == 1:
            create_insurance_office(series=series, name=name, location=address, region=region, director=director,
                                    created_by=created_by, office_type=office_type, parent=parent,
                                    funded=founded_date, bank_ids=bank_ids, phone_number=contact)
        else:
            insurance_office = InsuranceOffice.objects.get(id=office_id)
            is_exist = request.data.get('is_exist', insurance_office.is_exist)
            phone_number = insurance_office.contact if contact is None else contact
            parent_id = insurance_office.parent.id if parent_id is None else parent_id
            created_by = insurance_office.cr_by if created_by is None else created_by
            if parent_id is not None:
                parent = InsuranceOffice.objects.get(id=parent_id)

            edit_insurance_office(office_id=office_id, series=series, name=name, location=address, region=region,
                                  director=director, office_type=office_type, parent=parent,
                                  bank_ids=bank_ids, phone_number=phone_number,
                                  funded=founded_date if founded_date is None else insurance_office.founded_date,
                                  is_exist=is_exist, created_by=created_by)
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = e.__str__()

    return JsonResponse(response)


def generate_page_size(page=None, size=None):
    if page is None or size is None:
        return [0, 0]
    return [page, size]


@api_view(['POST'])
def is_login_exists(request):
    response = {}
    try:
        login = request.data.get('login')
        is_free_login(login=login)
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = e.__str__()

    return JsonResponse(response)


@api_view(['GET'])
def get_product_type_fields(request):
    type_id = request.query_params.get('product_type_id', None)
    response = {}
    try:
        objs = ProductField.objects.filter(product_id=type_id)
        serializer = ProductFieldsSerializer(objs, many=True)
        response['data'] = serializer.data
        response['success'] = True
    except Exception as e:
        response['error_msg'] = e.__str__()
        response['success'] = False
    return JsonResponse(response)

# @api_view(['GET'])
# def get_prduct_details(request)

class PolicyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Policy.objects.all()
    serializer_class = PoliciesSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request, *args, **kwargs):
        page = request.query_params.get('page', 1)
        size = request.query_params.get('size', 20)
        is_non_transferred = (request.query_params.get('nonTransferred', 'false')).lower()
        response = {}

        try:
            items = 0
            if is_non_transferred == 'true':
                items = Policy.objects.filter(policytransfers__to_office__isnull=True)
            else:
                items = Policy.objects.all()

            paginator = Paginator(items, size)
            serializer = PoliciesSerializer(paginator.page(page), many=True)
            response['data'] = serializer.data
            response['success'] = True
        except Exception as e:
            response['error_msg'] = e.__str__()
            response['success'] = False

        response['page'] = page
        response['size'] = size
        return Response(response)

    def create(self, request, *args, **kwargs):

        return Response({})


class TransferPoliciesViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = PolicyTransfers.objects.all()
    serializer_class = TransferPoliciesSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request):
        page = request.query_params.get('page', 1)
        size = request.query_params.get('size', 20)
        retransferred = request.query_params.get('retransferred', False)

        response = {}
        try:
            if not retransferred:
                items = PolicyTransfers.objects.all()
                paginator = Paginator(items, size)
                serializer = TransferPoliciesSerializer(paginator.page(page), many=True)
                response['data'] = serializer.data
                response['success'] = True
            else:
                items = PolicyRetransfer.objects.all()
                paginator = Paginator(items, size)
                serializer = RetransferPoliciesSerializer(paginator.page(page), many=True)
                response['data'] = serializer.data
                response['success'] = True

        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.__str__()

        response['page'] = page
        response['size'] = size
        return Response(response)

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            # request.user.permission_set
            to_branch_id = request.data.get('to_office', None)
            to_user_id = request.data.get('to_user', None)
            policy_ids = list(request.data.get('policies', []))
            if request.user.is_superuser and to_branch_id is not None:
                to_branch = InsuranceOffice.objects.get(id=to_branch_id)

                for i in policy_ids:
                    policy = Policy.objects.get(id=i)
                    obj = PolicyTransfers.objects.create(to_office=to_branch, policy=policy, cr_on=datetime,
                                                         cr_by=request.user)
                    obj.save()

                response['data'] = request.data
                response['success'] = True

            elif is_user_worker_of_director(director=request.user, user_id=to_user_id):
                to_user = OfficeWorkers.objects.get(user_id=to_user_id, office__director=request.user).user

                for i in policy_ids:
                    transfer = PolicyTransfers.objects.get(policy=i)
                    obj = PolicyRetransfer.objects.create(transfer=transfer, to_user=to_user, cr_on=datetime,
                                                          cr_by=request.user)
                    obj.save()

                response['data'] = request.data
                response['success'] = True
            else:
                response['error_msg'] = 'Only admin can access'
                response['success'] = False
        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.__str__()
        return Response(response)


class PolicyIncomeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = PoliciesIncome.objects.all()
    serializer_class = PoliciesIncomeSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request):
        page = request.query_params.get('page', 1)
        size = request.query_params.get('size', 20)
        response = {}
        try:
            items = PoliciesIncome.objects.all()
            paginator = Paginator(items, size)

            serializer = PoliciesIncomeSerializer(paginator.page(page), many=True)
            response['data'] = serializer.data
            response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.__str__()

        response['page'] = page
        response['size'] = size
        return Response(response)

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.method == 'POST':
                params = self.request.data
                from_user = User.objects.get(username=params['from_username'])
                series = params['policy_series']
                policy_series_type = None

                is_free_policy = request.data.get('is_free_policy', None)  # bool(params['is_free_policy'])

                if series != '' and series is not None:
                    policy_series_type = PolicySeriesType.objects.get(id=series)
                    is_free_policy = False
                else:
                    is_free_policy = True
                if is_valid_policies_range(is_free_policy, series, params['from_number'],
                                           params['to_number']) is not True:
                    response['success'] = False
                    return Response(response)

                new_object = PoliciesIncome.objects.create(
                    act_number=params['act_number'],
                    act_date=datetime.now(),
                    policy_series=policy_series_type,
                    document=request.FILES['file'],
                    from_user=from_user,
                    policy_number_to=params['to_number'],
                    policy_number_from=params['from_number'],
                    is_free_policy=is_free_policy,
                    cr_by=self.request.user,
                )
                new_object.save()

                generate_policies(from_number=params['from_number'], to_number=params['to_number'],
                                  series=series, is_free_generated=is_free_policy, session=new_object)

                response['success'] = True
            else:
                response['success'] = False
        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.args
            print(e)
        return Response(response)


class PositionsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                Position.objects.create(
                    name=params['name']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Position.objects.get(id=item_id)
                serializer = PositionSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                Position.objects.filter(id=params['id']).update(
                    name=params['name']
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                params = self.request.data['params']
                Position.objects.filter(id=params['id']).update(
                    is_exist=True
                )
                response['success'] = True
            elif self.request.data['action'] == 'list':
                items = Position.objects.filter(is_exist=True)
                serializer = PositionSerializer(items, many=True)
                response['data'] = serializer.data
                response['success'] = True
        except Exception as e:
            print(e)
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        # print(json.loads(self.request.query_params.get('filter_param'))["status"])
        queryset = Profile.objects.all()
        return queryset


class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class GridViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Dt_Option.objects.all()
    serializer_class = DtOptionSerializer

    def create(self, request, *args, **kwargs):
        if Dt_Option.objects.filter(codeName=request.data['gridCodeName']).exists():
            grid = Dt_Option.objects.get(codeName=request.data['gridCodeName'])
            serializer = DtOptionSerializer(grid, read_only=True)
            return Response(serializer.data)


class IndividualClientViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = IndividualClient.objects.all()
    serializer_class = IndividualClientSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                IndividualClient.objects.create(
                    first_name=params['first_name'],
                    last_name=params['last_name'],
                    middle_name=params['middle_name'],
                    address=params['address'],
                    phone_number=params['phone_number'],
                    cr_by=self.request.user
                ).save()
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = IndividualClient.objects.get(id=item_id)
                serializer = IndividualClientSerializer(item)
                response['success'] = True
                response['data'] = serializer.data
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                IndividualClient.objects.filter(id=params['id']).update(
                    first_name=params['first_name'],
                    last_name=params['last_name'],
                    middle_name=params['middle_name'],
                    address=params['address'],
                    phone_number=params['phone_number'],
                    up_by=self.request.user,
                    up_on=datetime.datetime.now()
                )
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                IndividualClient.objects.filter(id=item_id).update(
                    is_exist=False
                )
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class CurrencyViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Currency.objects.filter(is_exist=True)
    serializer_class = CurrencySerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                Currency.objects.create(
                    name=params['name'],
                    code=params['code']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Currency.objects.get(id=item_id)
                serializer = CurrencySerializer(item)
                response['success'] = True
                response['data'] = serializer.data
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                Currency.objects.filter(id=params['id']).update(
                    name=params['name'],
                    code=params['code']
                )
                response['success'] = True
            elif self.request.data['delete']:
                params = self.request.data['params']
                Currency.objects.filter(id=params['id']).update(
                    is_exist=False
                )
                response['success'] = True
        except Exception as e:
            print(e)
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class ClassifiersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductTypeCode.objects.filter(is_exist=True)
    serializer_class = ClassifiersSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                ProductTypeCode.objects.create(
                    name=params['name']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = ProductTypeCode.objects.get(id=item_id)
                serializer = ClassifiersSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                ProductTypeCode.objects.filter(id=params['id'], is_exist=True).update(
                    name=params['name']
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                ProductTypeCode.objects.filter(id=item_id).update(
                    is_exist=False
                )
                response['success'] = True
            elif self.request.data['action'] == 'list':
                items = ProductTypeCode.objects.filter(is_exist=True)
                serializer = ClassifiersSerializer(items)
                response['data'] = serializer.data
                response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class ProductTypeViewSet(viewsets.ViewSet):
    queryset = ProductType.objects.all()
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def __handle_request(req):
        response = {}
        try:
            create_update_product_type(request=req)
            response['success'] = True
        except Exception as e:
            response['error_msg'] = e.__str__()
            response['success'] = False
        return Response(response)

    def create(self, request, *args, **kwargs):
        return self.__handle_request(req=request)

    def put(self, request, *args, **kwargs):
        return self.__handle_request(req=request)

    def get(self, request, *args, **kwargs):
        client_type = request.query_params.get('client_type', None)

        if client_type is not None:
            serializer = ProductSerializer(ProductType.objects.filter(client_type=client_type), many=True)
        else:
            serializer = ProductSerializer(ProductType.objects.all(), many=True)

        response = {
            'data': serializer.data,
            'success': True
        }

        return JsonResponse(response)


class ProductTypeCodeViewSet(viewsets.ViewSet):
    queryset = ProductTypeCode.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProductTypeCodeSerializer

    @staticmethod
    def __handle_request(req):
        response = {}
        try:
            create_update_product_type_code(request=req)
            response['success'] = True
        except Exception as e:
            response['error_msg'] = e.__str__()
            response['success'] = False
        return Response(response)

    def create(self, request, *args, **kwargs):
        return self.__handle_request(req=request)

    def put(self, request, *args, **kwargs):
        return self.__handle_request(req=request)

    def get(self, request, *args, **kwargs):
        serializer = ProductTypeCodeSerializer(ProductTypeCode.objects.all(), many=True)

        response = {
            'data': serializer.data,
            'success': True
        }

        return JsonResponse(response)
    # def get(self, request, *args, **kwargs)


class BankViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Bank.objects.filter(is_exist=True)
    serializer_class = BankSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            Bank.objects.create(
                name=request.data.get('name', None),
                branchName=request.data.get('branch_name', None),
                mfo=request.data.get('mfo', None),
                inn=request.data.get('inn', None),
                address=request.data.get('address', None),
                phone_number=request.data.get('phone_number', None),
                checking_account=request.data.get('checking_account', None)
            ).save()
            response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class BranchViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = InsuranceOffice.objects.filter(is_exist=True)
    serializer_class = BranchSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request):
        page = request.query_params.get('page', 1)
        size = request.query_params.get('size', 20)
        response = {}
        try:
            items = InsuranceOffice.objects.all()
            paginator = Paginator(items, size)

            serializer = BranchSerializer(paginator.page(page), many=True)
            response['data'] = serializer.data
            response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.__str__()

        response['page'] = page
        response['size'] = size
        return Response(response)

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                director = User.objects.get(id=params['director'])
                InsuranceOffice.objects.create(
                    name=params['name'],
                    director=director,
                    cr_by=self.request.user
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = InsuranceOffice.objects.get(id=item_id)
                serializer = BranchSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                director = User.objects.get(id=params['director'])
                InsuranceOffice.objects.filter(id=params['id']).update(
                    name=params['name'],
                    director=director,
                    up_by=self.request.user
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                InsuranceOffice.objects.filter(id=item_id).update(
                    up_by=self.request.user,
                    is_exist=False
                )
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class LegalClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = LegalClient.objects.filter(is_exist=True)
    serializer_class = LegalClientSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                LegalClient.objects.create(
                    name=params['name'],
                    address=params['address'],
                    phone_number=params['phone_number']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = LegalClient.objects.get(id=item_id)
                response['data'] = LegalClientSerializer(item)
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                LegalClient.objects.filter(id=params['id']).update(
                    name=params['name'],
                    address=params['address'],
                    phone_number=params['phone_number'],
                    up_by=self.request.user
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                LegalClient.objects.filter(id=item_id).update(
                    up_by=self.request.user,
                    is_exist=False
                )
                response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            # create user
            if self.request.method == 'POST':
                login = request.data.get('login')
                email = request.data.get('email', None)
                password = request.data.get('password')
                phone_number = request.data.get('phone_number', None)
                status = request.data.get('is_active', None)
                position = Position.objects.get(id=request.data.get('position_id'))
                first_name = request.data.get('first_name')
                last_name = request.data.get('last_name')
                middle_name = request.data.get('middle_name', None)
                passport_number = request.data.get('passport_number')
                passport_series = request.data.get('passport_series')

                passport_given_by = request.data.get('passport_given_by', None)
                passport_given_date = request.data.get('passport_given_date', None)

                document = request.FILES['file']
                image = request.FILES.get('image', None)
                created_by = request.user

                new_user = create_user(login=login, email=email, password=password, is_active=status,
                                       first_name=first_name,
                                       last_name=last_name, )

                create_status = register_user_profile(user=new_user,
                                                      position=position,
                                                      middle_name=middle_name,
                                                      phone_number=phone_number,
                                                      passport_number=passport_number,
                                                      passport_series=passport_series,
                                                      document=document,
                                                      passport_given_date=passport_given_date,
                                                      passport_given_by=passport_given_by,
                                                      created_by=created_by, image=image)

                print(f'new user create status {create_status}')

                response['success'] = True

        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.args
            print(e)
        return Response(response)

    def put(self, request, *args, **kwargs):
        response = {}
        try:
            edit_profile(self.request)
            response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.args
            print(e)
        return Response(response)


class ApplicationFormViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = ApplicationForm.objects.all()

    def create(self, request):
        response = {}
        try:
            product_type = ProductType.objects.get(id=request.data.get('product_type'))

            person = request.data.get('client', None)

            legal_client = None
            individual_client = None

            is_legal_client = person.get('is_legal_client', False)

            title = person.get('legal_client_title')
            first_name = person.get('first_name', None)
            last_name = person.get('last_name', None)

            passport_number = person.get('passport_number', None)
            passport_series = person.get('passport_series', None)
            passport_given_by = person.get('passport_given_by', None)
            passport_given_date = person.get('passport_given_date', None)

            address = person.get('client_address')
            client_phone_number = person.get('client_phone_number')
            mfo = person.get('request')

            client_bank_inn = person.get('client_bank_inn')

            client_bank_id = person.get('client_bank_id', None)

            if is_legal_client:
                legal_client = LegalClient.objects.update_or_create(mfo=mfo,
                                                                    defaults={
                                                                        'mfo': mfo,
                                                                        'title': title,
                                                                        'address': address,
                                                                        'client_phone_number': client_phone_number,

                                                                    })

            beneficiary = request.data.get('beneficiary', None)

            is_beneficiary_legal = beneficiary.get('is_beneficiary_legal', False)

            beneficiary_title = beneficiary.get('beneficiary_title', None)

            beneficiary_first_name = beneficiary.get('beneficiary_first_name', None)
            beneficiary_last_name = beneficiary.get('beneficiary_last_name', None)

            beneficiary_passport_series = beneficiary.get('beneficiary_passport_series', None)
            beneficiary_passport_number = beneficiary.get('beneficiary_passport_number', None)

            beneficiary_address = beneficiary.get('beneficiary_address', None)
            beneficiary_bank = None

            beneficiary_bank_id = beneficiary.get('beneficiary_bank_id', None)

            if beneficiary_bank_id is not None:
                beneficiary_bank = Bank.objects.get()

            beneficiary_number = beneficiary.get('beneficiary_number', None)
            beneficiary_mfo = beneficiary.get('beneficiary_mfo', None)

            pledger = request.data.get('pledger', None)

            pledger_name = pledger.get('pledger_name', None)
            pledger_address = pledger.get('pledger_address', None)
            pledger_number = pledger.get('pledger_phone_number', None)
            pledger_bank_account = pledger.get('pledger_checking_account', None)

            pledger_bank_id = pledger.get('pledger_bank_id', None)
            pledger_bank = None
            if beneficiary_bank_id is not None:
                pledger_bank = Bank.objects.get()

            pledger_inn = pledger.get('pledger_inn', None)
            pledger_mfo = pledger.get('pledger_mfo', None)

            from_date = request.data.get('from_date')

            to_date = request.data.get('to_date')

            contract_type = request.data.get('contract_type_id')
            form_status = request.data.get('form_status')
            fields = request.data.get('fields', [])

            for field in fields:
                field_type = field.get('type', None)
                input_type = field.get('input_type')
                is_required = field.get('is_required')
                name = field.get('name')
                value = field.get('value')
                order = field.get('order')
                pass

            response['success']=True
        except Exception as e:
            response['error_msg'] = e.__str__()
            response['success'] = False
        return Response(response)