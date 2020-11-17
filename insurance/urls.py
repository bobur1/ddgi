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
router.register('registered-policies', viewset=views.RegisterPoliseViewSet)
router.register('currency', viewset=views.CurrencyViewset)
router.register('group', viewset=views.GroupViewset)
router.register('klass', viewset=views.KlassViewset)
router.register('vid', viewset=views.VidViewset)
router.register('bank', viewset=views.BankViewset)
router.register('branch', viewset=views.BranchViewSet)
router.register('product', viewset=views.ProductViewSet)
router.register('policies-incomes', viewset=views.PolicyIncomeViewSet)
router.register('policies', viewset=views.PolicyViewSet)
router.register('policy-transfers', viewset=views.TransferPoliciesViewSet)

urlpatterns = [
                  path('', controller.home),
                  path('test/', views.test_view),
                  path('api/', include(router.urls)),
                  path('api/product-fields/', views.product_fields),
                  path('api/policy-series/', views.policy_series),
                  path('api/get-my-workers/', views.get_my_workers),
                  path('api/get-my-branches/', views.get_my_branches),
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
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
