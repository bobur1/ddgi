from django.urls import path, include
from insurance import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from insurance import controller

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
                  path('legal-client/', controller.legal_client, name='legal_client'),
                  path('legal-client/add/', controller.legal_client_add, name='legal_client_add'),
                  path('polis-registration/', controller.polis_registration, name='polis_registration'),
                  path('polis-registration/add/', controller.polis_registration_add, name='polis_registration_add'),

              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
