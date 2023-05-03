from django.urls import path
from .views import *
urlpatterns = [
    path('crops-data/',cropsdetail,name='cropsdetail'),
    path('login/',login,name='login'),
    path('seller-data/',get_seller_data,name='seller-data'),
]