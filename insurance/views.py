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
import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def test_view(request):
    response = {'success': True, 'authenticated_user': request.user.username}
    return Response(response)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def is_valid_policies_range(is_freely_generated, series, from_number, to_number):
    s_id = 'NULL'
    if series != '' and series is not None:
        s_id = int(series)
    query = 'SELECT * FROM insurance_policy where series_id is {} AND policy_number>={}'.format(s_id, from_number)
    objs = Policy.objects.raw(raw_query=query)
    result = objs.__len__() == 0
    return result


def generate_policies(from_number, to_number, is_free_generated, series, session):
    for i in range(int(from_number), int(to_number)+1):
        s = None
        if series != '' and series is not None:
            s = PolicySeriesType.objects.get(id=series)

        # session = PoliciesIncome.objects.get(id = session_id)
        Policy.objects.create(policy_number=i,
                              series=s,
                              is_free_generated=is_free_generated,
                              income_session=session).save()


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


def generatePageSize(page=None, size=None):
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
                items = Policy.objects.filter(policytransfers__policies__policy_number__isnull=True)
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
        response = {}
        try:
            items = PolicyTransfers.objects.all()
            paginator = Paginator(items, size)

            serializer = TransferPoliciesSerializer(paginator.page(page), many=True)
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
            to_branch_id = request.data.get('to_branch', None)
            to_branch = Branch.objects.get(id=to_branch_id)
            to_user_id = request.data.get('to_user', None)
            to_user = None

            policy_ids = list(request.data.get('policies', []))
            # policies = Policy.objects.raw("SELECT * FROM insurance_policy where id in {}".format(policy_ids))

            if to_user_id is not None:
                to_user = User.objects.get(id=to_user_id)

            obj = PolicyTransfers.objects.create(to_branch=to_branch, to_user=to_user, cr_on=datetime, cr_by=request.user)
            obj.save()
            for i in policy_ids:
                obj.policies.add(i)

            response['data'] = request.data
            response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = e.__str__()
        return Response(response)


    # to_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)
    # to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    # policies = models.ManyToManyField(Policy)
    # cr_on = models.DateTimeField(auto_now_add=True)
    # cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
    #                           related_name='policy_transfers_cr_by')


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
    #permission_classes = [IsAuthenticated, ]
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


class RegisterPoliseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = RegisteredPolises.objects.filter(is_exist=True)
    serializer_class = RegisteredPoliseSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        # req = json.loads(self.request.data)
        try:
            if str(self.request.data['action']) == 'create':
                params = json.loads(self.request.data['params'])
                RegisteredPolises.objects.create(
                    act_number=params['act_number'],
                    act_date=params['act_date'],
                    polis_number_from=params['polis_number_from'],
                    polis_number_to=params['polis_number_to'],
                    polis_quantity=params['polis_quantity'],
                    polis_status=params['polis_status'],
                    document=self.request.FILES['file'],
                    cr_by=self.request.user
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = RegisteredPolises.objects.get(id=item_id)
                serializer = RegisteredPoliseSerializer(item)
                response['data'] = serializer.data
            elif str(self.request.data['action']) == 'update':
                print(self.request.content_type)
                print(self.request.data)
                print(self.request.FILES)
                if self.request.FILES['file']:
                    print(self.request.data)
                    print(self.request.FILES)
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


class GroupViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                Group.objects.create(
                    name=params['name']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Group.objects.get(id=item_id)
                serializer = GroupSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['params'] == 'update':
                params = self.request.data['params']
                Group.objects.filter(id=params['id']).update(
                    name=params['name']
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                Group.objects.filter(id=item_id).update(
                    is_exist=False
                )
                response['success'] = True
            elif self.request.data['action'] == 'list':
                items = Group.objects.filter(is_exist=True)
                serializer = GroupSerializer(items, many=True)
                response['data'] = serializer.data
                response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class KlassViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Klass.objects.filter(is_exist=True)
    serializer_class = KlassSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                Klass.objects.create(
                    name=params['name']
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Klass.objects.get(id=item_id)
                serializer = KlassSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                Klass.objects.filter(id=params['id'], is_exist=True).update(
                    name=params['name']
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                Klass.objects.filter(id=item_id).update(
                    is_exist=False
                )
                response['success'] = True
            elif self.request.data['action'] == 'list':
                items = Klass.objects.filter(is_exist=True)
                serializer = KlassSerializer(items)
                response['data'] = serializer.data
                response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class VidViewset(viewsets.ModelViewSet):
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


class BankViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Bank.objects.filter(is_exist=True)
    serializer_class = BankSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                Bank.objects.create(
                    name=params['name'],
                    mfo=params['mfo'],
                    inn=params['inn'],
                    address=params['address'],
                    phone_number=params['phone_number'],
                    checking_account=params['checking_account']

                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Bank.objects.get(id=item_id, is_exist=True)
                serializer = BankSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                Bank.objects.filter(id=params['id'], is_exist=True).update(
                    name=params['name'],
                    mfo=params['mfo'],
                    inn=params['inn'],
                    address=params['address'],
                    phone_number=params['phone_number'],
                    checking_account=params['checking_account']

                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                Bank.objects.filter(id=item_id).update(
                    is_exist=False
                )
                response['success'] = True
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)


class BranchViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Branch.objects.filter(is_exist=True)
    serializer_class = BranchSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request):
        page = request.query_params.get('page', 1)
        size = request.query_params.get('size', 20)
        response = {}
        try:
            items = Branch.objects.all()
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
                Branch.objects.create(
                    name=params['name'],
                    director=director,
                    cr_by=self.request.user
                ).save()
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                item = Branch.objects.get(id=item_id)
                serializer = BranchSerializer(item)
                response['data'] = serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                director = User.objects.get(id=params['director'])
                Branch.objects.filter(id=params['id']).update(
                    name=params['name'],
                    director=director,
                    up_by=self.request.user
                )
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                Branch.objects.filter(id=item_id).update(
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


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductType.objects.filter(is_exist=True)
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = {}
        try:
            if self.request.data['action'] == 'create':
                params = self.request.data['params']
                klass = Klass.objects.get(id=params['klass'])
                group = Group.objects.get(id=params['klass'])
                vid = Vid.objects.get(id=params['vid'])
                new_product = ProductType.objects.create(
                    name=params['name'],
                    klass=klass,
                    group=group,
                    vid=vid
                ).save()
                fields = self.request.data['params']['fields']
                for f in fields:
                    ProductField.objects.create(
                        product=new_product,
                        type=f['type'],
                        name=f['name'],
                        value=f['value'],
                        order=f['order']
                    ).save()
                response['success'] = True
            elif self.request.data['action'] == 'update':
                params = self.request.data['params']
                klass = Klass.objects.get(id=params['klass'])
                group = Group.objects.get(id=params['group'])
                vid = Vid.objects.get(id=params['vid'])
                ProductType.objects.filter(id=params['id']).update(
                    klass=klass,
                    group=group,
                    vid=vid
                )
                response['success'] = True
            elif self.request.data['action'] == 'get':
                item_id = self.request.data['id']
                product = ProductType.objects.get(id=item_id)
                product_fields = ProductField.objects.get(product=product)
                product_serializer = ProductSerializer(product)
                product_field_serializer = ProductFieldsSerializer(product_fields, many=True)
                response['data']['product'] = product_serializer.data
                response['data']['product_fields'] = product_field_serializer.data
                response['success'] = True
            elif self.request.data['action'] == 'delete':
                item_id = self.request.data['id']
                ProductType.objects.filter(id=item_id).update(
                    is_exist=False
                )
        except Exception as e:
            response['success'] = False
            response['error_msg'] = str(e)
        return Response(response)
