from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from insurance.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include('insurance.urls')),
    path('docs/', include_docs_urls(title='My API title'))

]
