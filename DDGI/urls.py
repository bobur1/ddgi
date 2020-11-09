from django.contrib import admin
from django.urls import path, include
from insurance.views import MyTokenObtainPairView
from django.contrib.auth import views as authview


urlpatterns = [

    path('admin/', admin.site.urls),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', authview.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authview.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', include('insurance.urls'))
]
