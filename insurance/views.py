from insurance.helpers import *

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
def create_office(request):
    response = {}
    try:
        series = request.data.get('series')
        director_id = request.data.get('director_id')
        director = User.objects.get(id=director_id)
        created_by = request.user
        office_type = OfficeType.objects.get(id=request.data.get('office_type'))
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

        create_insurance_office(series=series, name=name, location=address, region=region, director=director,
                                created_by=created_by, office_type=office_type, parent=parent, funded=founded_date)
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = e.__str__()

    return JsonResponse(response)


def generate_page_size(page=None, size=None):
    if page is None or size is None:
        return [0, 0]
    return [page, size]


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

                is_free_policy = bool(params['is_free_policy'])

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
                    act_date=datetime.datetime.now(),
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
            # elif self.request.method == 'GET':
            #     items = PoliciesIncome.objects.all()
            #     serializer = PoliciesIncomeSerializer(items, many=True)
            #     response['data'] = serializer
            #     response['success'] = True
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


class VidViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Vid.objects.filter(is_exist=True)
    serializer_class = VidSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                Vid.objects.create(
                    name=params['name']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Vid.objects.get(id=item_id)
                serializer = VidSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                Vid.objects.filter(id=params['id']).update(
                    name=params['name']
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                Vid.objects.filter(id=item_id).update(
                    is_exixst=False
                )

        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


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

