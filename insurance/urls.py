from django.urls import path, include
from insurance import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from insurance import controller
from django.contrib.auth import views as authview


router = routers.DefaultRouter()

router.register('position', viewset=views.PositionsViewSet)
router.register('profile', viewset=views.ProfileViewSet)
router.register('permission', viewset=views.PermissionViewSet)
router.register('grid', viewset=views.GridViewSet)
router.register('client-individual', viewset=views.IndividualClientViewSet)
router.register('client-legal', viewset=views.LegalClientViewSet)
router.register('currency', viewset=views.CurrencyViewset)
router.register('klass', viewset=views.ClassifiersViewSet)
router.register('vid', viewset=views.VidViewSet)
router.register('bank', viewset=views.BankViewSet)
router.register('branch', viewset=views.BranchViewSet)
router.register('policies-incomes', viewset=views.PolicyIncomeViewSet)
router.register('policies', viewset=views.PolicyViewSet)
router.register('policy-transfers', viewset=views.TransferPoliciesViewSet)
router.register('user_creat_update', viewset=views.UserViewSet)
router.register('product_type', viewset=views.ProductTypeViewSet)
router.register('product_type_codes', viewset=views.ProductTypeCodeViewSet)


urlpatterns = [
    path('api/product-fields/', views.product_fields),
    path('api/policy-series/', views.policy_series),
    path('api/deactivate-policy/', views.deactivate_policy),
    path('api/create-office/', views.create_update_office),
    path('api/update-office/', views.create_update_office),
    path('api/check_login/', views.is_free_login),
]

urlpatterns += [
                  path('', controller.home),
                  path('test/', views.test_view),
                  path('api/', include(router.urls)),
                  path('individual-client/', controller.individual_client, name='individual_client'),
                  path('individual-client/add/', controller.individual_client_add, name='individual_client_add'),
                  path('login/', authview.LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', authview.LogoutView.as_view(template_name='logout.html'), name='logout'),
                  path('individual-client/', controller.individual_client, name='individual_client'),
                  path('individual-client/add/', controller.individual_client_add, name='individual_client_add'),
                  path('individual-client/<int:id>/', controller.individual_client_show, name='individual_client_show'),
                  path('individual-client/<int:id>/edit/', controller.individual_client_edit, name='individual_client_edit'),
                  path('legal-client/', controller.legal_client, name='legal_client'),
                  path('legal-client/add/', controller.legal_client_add, name='legal_client_add'),
                  path('legal-client/<int:id>/', controller.legal_client_show, name='legal_client_show'),
                  path('legal-client/<int:id>/edit/', controller.legal_client_edit, name='legal_client_edit'),
                  path('polis-registration/', controller.polis_registration, name='polis_registration'),
                  path('polis-registration/add/', controller.polis_registration_add, name='polis_registration_add'),
                  path('polis-transfer/', controller.polis_transfer_list, name='polis_transfer'),
                  path('polis-transfer/add/', controller.polis_transfer, name='polis_transfer_add'),
                  path('polis-retransfer/', controller.polis_retransfer_list, name='polis_retransfer'),
                  path('polis-retransfer/add/', controller.polis_retransfer, name='polis_retransfer_add'),
                  path('request/add/', controller.request, name='request_add'),
                  path('user', controller.user, name='user'),
                  path('user/add', controller.user_add, name='user_add'),
                  path('user/<int:id>', controller.user_show, name='user_show'),
                  path('user/<int:id>/edit', controller.user_edit, name='user_edit'),
                  path('references/bank/', controller.bank, name='bank'),
                  path('references/bank/add/', controller.bank_add, name='bank_add'),
                  path('references/bank/<int:id>/', controller.bank_show, name='bank_show'),
                  path('references/bank/<int:id>/edit/', controller.bank_edit, name='bank_edit'),
                  path('references/currency/', controller.currency, name='currency'),
                  path('references/currency/add/', controller.currency_add, name='currency_add'),
                  path('references/currency/<int:id>/', controller.currency_show, name='currency_show'),
                  path('references/currency/<int:id>/edit/', controller.currency_edit, name='currency_edit'),
                  path('references/view/', controller.view, name='view'),
                  path('references/view/add/', controller.view_add, name='view_add'),
                  path('references/view/<int:id>/', controller.view_show, name='view_show'),
                  path('references/view/<int:id>/edit/', controller.view_edit, name='view_edit'),
                  path('references/branch/', controller.branch, name='branch'),
                  path('references/branch/add/', controller.branch_add, name='branch_add'),
                  path('references/branch/<int:id>/', controller.branch_show, name='branch_show'),
                  path('references/branch/<int:id>/edit/', controller.branch_edit, name='branch_edit'),
                  path('references/klass/', controller.klass, name='klass'),
                  path('references/klass/add/', controller.klass_add, name='klass_add'),
                  path('references/klass/<int:id>/', controller.klass_show, name='klass_show'),
                  path('references/klass/<int:id>/edit/', controller.klass_edit, name='klass_edit'),
                  path('references/polis-series/', controller.polis_series, name='polis_series'),
                  path('references/polis-series/add/', controller.polis_series_add, name='polis_series_add'),
                  path('references/polis-series/<int:id>/', controller.polis_series_show, name='polis_series_show'),
                  path('references/polis-series/<int:id>/edit/', controller.polis_series_edit, name='polis_series_edit'),
                  # path('references/group/', controller.group, name='group'),
                  # path('references/group/add/', controller.group_add, name='group_add'),
                  # path('references/group/<int:id>/', controller.group_show, name='group_show'),
                  # path('references/group/<int:id>/edit/', controller.group_edit, name='group_edit'),
                  path('references/position', controller.position, name='position'),
                  path('references/position/add', controller.position_add, name='position_add'),
                  path('references/position/<int:id>', controller.position_show, name='position_show'),
                  path('references/position/<int:id>/edit', controller.position_edit, name='position_edit'),
                  path('product/', controller.product, name='product'),
                  path('product/add/', controller.product_add, name='product_add'),
                  path('product/<int:id>/', controller.product_show, name='product_show'),
                  path('product/<int:id>/edit/', controller.product_edit, name='product_edit'),
                  path('product/<int:product_id>/field/add/', controller.product_field_add, name='product_field_add'),
                  path('product/<int:product_id>/field/<int:id>/', controller.product_field_show, name='product_field_show'),
                  path('product/<int:product_id>/field/<int:id>/edit/', controller.product_field_edit, name='product_field_edit'),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
