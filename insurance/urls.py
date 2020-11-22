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
                  path('legal-client/', controller.legal_client, name='legal_client'),
                  path('legal-client/add/', controller.legal_client_add, name='legal_client_add'),
                  path('polis-registration/', controller.polis_registration, name='polis_registration'),
                  path('polis-registration/add/', controller.polis_registration_add, name='polis_registration_add'),
                  path('polis-transfer/', controller.polis_transfer_list, name='polis_transfer'),
                  path('polis-transfer/add/', controller.polis_transfer, name='polis_transfer_add'),
                  path('polis-retransfer/', controller.polis_retransfer_list, name='polis_retransfer'),
                  path('polis-retransfer/add/', controller.polis_retransfer, name='polis_retransfer_add'),
                  path('request/add', controller.request, name='request_add'),
                  path('spravochniki/bank/add', controller.spravochnik_bank, name='spravochnik_bank_add'),
                  path('user/add', controller.user, name='user_add'),
                  path('spravochniki/currency/', controller.currency, name='currency'),
                  path('spravochniki/currency/add/', controller.currency_add, name='currency_add'),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
