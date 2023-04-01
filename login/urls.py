from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.add_user,name='add_user'),
    path('login/', views.Login,name='login'),
    path('crops-data/',views.cropsdetail,name='cropsdetail'),
    path('kyc/',views.kyc,name='kyc'),
]