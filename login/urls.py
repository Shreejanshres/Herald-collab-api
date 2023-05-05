from django.urls import path
from .views import *
urlpatterns = [
    path('crops-data/', cropsdetail, name='cropsdetail'),
    path('login/', login, name='login'),
    path('seller-data/', get_seller_data, name='seller-data'),
    path('farmer-data/', get_farmer_data, name='farmer-data'),
    path('signup/', signup, name='signup'),
    path('addcrop/', add_crops, name='addcrop'),
    path('addevent', add_event, name='addevent'),
    path('event/', get_event, name='getevent'),
    path('kyc/', kyc, name='kyc'),
    path('displaykyc/', display_kyc, name='displaykyc'),
    path('forgetpass/', forget, name='forgetpass'),
]
