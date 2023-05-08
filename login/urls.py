from django.urls import path
from .views import *
urlpatterns = [
    path('crops-data/', cropsdetail, name='cropsdetail'),
    path('addcrop/', add_crops, name='addcrop'),
    path('deletecrop/', delete_crops, name='deletecrop'),
    path('crops-data/<int:id>/', display_crop, name='displaycrop'),


    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),

    path('seller-data/', get_seller_data, name='seller-data'),
    path('farmer-data/', get_farmer_data, name='farmer-data'),
    path('kyc/', kyc, name='kyc'),
    path('displaykyc/', display_kyc, name='displaykyc'),
    path('acceptkyc/', verify_kyc, name='verifykyc'),
    path('rejectkyc/', reject_kyc, name='rejectkyc'),
    path('forgetpassword/', forget, name='forgetpass'),
    path('update/', update_password, name='verify'),

    path('addevent/', add_event, name='addevent'),
    path('event/', get_event, name='getevent'),

]
