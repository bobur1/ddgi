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

urlpatterns = [
                  path('', controller.home),
                  path('test/', views.test_view),
                  path('api/', include(router.urls)),
                  path('api/product-fields/', views.product_fields),
                  path('api/policy-series/', views.policy_series),
                  path('api/deactivate-policy/', views.deactivate_policy),
                  path('api/create-office/', views.create_update_office),
                  path('api/update-office/', views.create_update_office),
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
                  path('request/add', controller.request, name='request_add'),
                  path('user/add', controller.user, name='user_add'),
                  path('spravochniki/bank/', controller.bank, name='bank'),
                  path('spravochniki/bank/add/', controller.bank_add, name='bank_add'),
                  path('spravochniki/bank/<int:id>/', controller.bank_show, name='bank_show'),
                  path('spravochniki/bank/<int:id>/edit/', controller.bank_edit, name='bank_edit'),
                  path('spravochniki/currency/', controller.currency, name='currency'),
                  path('spravochniki/currency/add/', controller.currency_add, name='currency_add'),
                  path('spravochniki/currency/<int:id>/', controller.currency_show, name='currency_show'),
                  path('spravochniki/currency/<int:id>/edit/', controller.currency_edit, name='currency_edit'),
                  path('spravochniki/view/', controller.view, name='view'),
                  path('spravochniki/view/add/', controller.view_add, name='view_add'),
                  path('spravochniki/view/<int:id>/', controller.view_show, name='view_show'),
                  path('spravochniki/view/<int:id>/edit/', controller.view_edit, name='view_edit'),
                  path('spravochniki/branch/', controller.branch, name='branch'),
                  path('spravochniki/branch/add/', controller.branch_add, name='branch_add'),
                  path('spravochniki/branch/<int:id>/', controller.branch_show, name='branch_show'),
                  path('spravochniki/branch/<int:id>/edit/', controller.branch_edit, name='branch_edit'),
                  path('spravochniki/klass/', controller.klass, name='klass'),
                  path('spravochniki/klass/add/', controller.klass_add, name='klass_add'),
                  path('spravochniki/klass/<int:id>/', controller.klass_show, name='klass_show'),
                  path('spravochniki/klass/<int:id>/edit/', controller.klass_edit, name='klass_edit'),
                  path('spravochniki/polis-series/', controller.polis_series, name='polis_series'),
                  path('spravochniki/polis-series/add/', controller.polis_series_add, name='polis_series_add'),
                  path('spravochniki/polis-series/<int:id>/', controller.polis_series_show, name='polis_series_show'),
                  path('spravochniki/polis-series/<int:id>/edit/', controller.polis_series_edit, name='polis_series_edit'),
                  # path('spravochniki/group/', controller.group, name='group'),
                  # path('spravochniki/group/add/', controller.group_add, name='group_add'),
                  # path('spravochniki/group/<int:id>/', controller.group_show, name='group_show'),
                  # path('spravochniki/group/<int:id>/edit/', controller.group_edit, name='group_edit'),
                  path('spravochniki/position/', controller.position, name='position'),
                  path('spravochniki/position/add/', controller.position_add, name='position_add'),
                  path('spravochniki/position/<int:id>/', controller.position_show, name='position_show'),
                  path('spravochniki/position/<int:id>/edit/', controller.position_edit, name='position_edit'),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
