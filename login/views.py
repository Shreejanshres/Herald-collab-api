from django.core.mail import send_mail
import random
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .models import *
from login.models import farmer
from .serializer import *
from django.core import serializers

from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('pass')
        print(email, password)
        if (farmer.objects.filter(email=email, password=password).exists()):
            print("farmer")
            data = get_object_or_404(farmer, email=email, password=password)
            response_data = {
                'id': data.id,
                'name': data.name,
                'address': data.address,
                'phone': data.phone,
                'email': data.email,
                'verified': data.is_verified,
                'type': 'farmer',
            }
            return JsonResponse(response_data)
        elif (seller.objects.filter(email=email, password=password).exists()):
            data = get_object_or_404(seller, email=email, password=password)
            response_data = {
                'id': data.id,
                'name': data.name,
                'address': data.address,
                'phone': data.phone,
                'email': data.email,
                'type': 'seller'
            }
            return JsonResponse(response_data)
        elif (admin.objects.filter(email=email, password=password).exists()):
            data = get_object_or_404(admin, email=email, password=password)
            print(data)
            response_data = {
                email: data.email,
                password: data.password,
                'type': 'admin'
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'success': False, 'message': 'Usernot found'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


def getimage(id):
    obj = farmer.objects.get(id=id)
    image_data = obj.profilepic.read()
    return serializers.serialize("json", [obj, ])


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        address = data.get('address')
        phone = data.get('phone')
        user = data.get('user')
        print(email, password, address, phone, user)
        if user == 'farmer':
            res = farmer.objects.filter(email=email)
            print(res)
            if res:
                return JsonResponse({'success': False, 'message': 'Email already exists'})
            else:
                data = farmer.objects.create(
                    email=email, password=password, address=address, phone=phone)
                print(data)
                data.save()
                response_data = {
                    'type': 'farmer',
                    'id': data.id,

                }
            return JsonResponse(response_data)

        elif user == 'seller':
            res = seller.objects.filter(email=email)
            if res:
                return JsonResponse({'success': False, 'message': 'Email already exists'})
            else:
                data = seller.objects.create(
                    email=email, password=password, address=address, phone=phone)
                data.save()
                response_data = {
                    'type': 'seller',
                    'id': data.id,
                }
            return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
def kyc(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        name = data.get('name')
        citizenf = data.get('citifront')
        citizenb = data.get('citiback')
        profile = data.get('proimg')
        print(id, name, citizenf, citizenb, profile)
        res = farmer.objects.filter(id=id)
        print(res)
        if res:
            farmer.objects.filter(id=id).update(
                name=name, citizenship_front=citizenf, citizenship_back=citizenb, profilepic=profile)
            return JsonResponse({'success': True, 'message': 'Successfully Updated'})
        else:
            return JsonResponse({'success': False, 'message': ' Could not update'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@api_view(['GET'])
def display_kyc(request):
    unverified_farmers = farmer.objects.filter(is_verified=False)
    serializer = farmerserializer(unverified_farmers, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def verify_kyc(request):
    print("yolo")
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        print(id)
        farmer.objects.filter(id=id).update(is_verified=True)
        return JsonResponse({'success': True, 'message': 'Successfully Verified'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
def reject_kyc(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        print(id)
        farmer.objects.filter(id=id).delete()
        return JsonResponse({'success': True, 'message': 'Successfully Rejected'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
def add_crops(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        region = data.get('region')
        province = data.get('province')
        temperature = data.get('temperature')
        climate = data.get('climate')
        soil = data.get('soil')
        rain = data.get('rain')
        disease = data.get('disease')
        nutrient = data.get('nutrient')
        print(name, region, province, temperature,
              climate, soil, rain, disease, nutrient)

        response = cropdetail.objects.create(name=name, region=region, province=province, temperature=temperature,
                                             climate=climate, soil=soil, rain=rain, disease=disease, nutrient=nutrient)
        response.save()
        return JsonResponse({'sucess': True, 'message': 'Successfully Added'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
def delete_crops(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        print(id)
        cropdetail.objects.filter(id=id).delete()
        return JsonResponse({'success': True, 'message': 'Successfully Deleted'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@api_view(['GET'])
def cropsdetail(request):  # get request from the frontend
    crops = cropdetail.objects.all()  # get all the data from the database
    serializer = cropdetailserializer(crops, many=True)
    return Response(serializer.data)  # return the data to the frontend


@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('eventname')
        date = data.get('eventdate')
        time = data.get('eventtime')
        description = data.get('eventdesc')
        print(name, date, time, description)
        response = event.objects.create(
            eventname=name, eventdate=date, eventtime=time, eventdescription=description)
        response.save()
        return JsonResponse({'sucess': True, 'message': 'Successfully Added'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@api_view(['GET'])
def get_event(request):
    even = event.objects.all()
    serializer = eventserializer(even, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['Get'])
def get_seller_data(request):
    data = seller.objects.all()
    serializer = sellerserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['Get'])
def get_farmer_data(request):
    data = farmer.objects.filter(is_verified=True)
    serializer = farmerserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@renderer_classes([JSONRenderer])
def forget(request):
    print("Inside forget")
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        print(email)
        otp = str(random.randint(100000, 999999))
        # Compose the email message
        subject = 'Your OTP for password reset'
        message = f'Your OTP is {otp}.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        # Send the email using Gmail
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=True)
        # Store the OTP in the session for later verification
        request.session['otp'] = otp
        request.session['email'] = email
        respose_data = {'otp': otp, 'success': True}
        return JsonResponse(respose_data)
    else:
        return JsonResponse({'success': True, 'message': 'Password changed successfully'})


# @csrf_exempt
# # code to get the otp from the user and verify it
# def verify(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         otp = data.get('otp')
#         if otp == request.session['otp']:
#             return JsonResponse({'success': True, 'message': 'OTP verified'})
#         else:
#             return JsonResponse({'success': False, 'message': 'OTP incorrect'})
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid Request'})

# code to take the id of user after the login and display the crop of the user

@csrf_exempt
def update_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('newpass')
        email = data.get('email')
        print(email)
        print(password)
        if (farmer.objects.filter(email=email).exists()):
            data = farmer.objects.get(email=email)
            data.password = password
            data.save()
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})
        elif (seller.objects.filter(email=email).exists()):
            data = seller.objects.get(email=email)
            data.password = password
            data.save()
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Not changed'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
@api_view(['GET'])
def display_crop(request, id):
    crop = get_object_or_404(cropdetail, id=id)
    serializer = cropdetailserializer(crop)
    return JsonResponse(serializer.data, safe=False)
