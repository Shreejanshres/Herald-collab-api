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
from .serializer import *
import requests
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
        try:
            data = get_object_or_404(farmer, email=email, password=password)
            response_data = {
                'id': data.id,
                'name': data.name,
                'address': data.address,
                'phone': data.phone,
                'email': data.email,
                'profilepic': data.profilepic.url,
                'verified': data.is_verified,
                'type': 'farmer'
            }
            print(response_data.get('profilepic'))
            return JsonResponse(response_data)
        except Exception as e:
            print(e)
            pass
        try:
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
        except:
            pass
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
        password = data.get('pass')
        address = data.get('address')
        phone = data.get('phone')
        user = data.get('user')
        print(email, password, address, phone, user)
        if user == 'farmer':
            res = farmer.objects.filter(email=email)
            if res:
                return JsonResponse({'success': False, 'message': 'Email already exists'})
            else:
                data = farmer.objects.create(
                    email=email, password=password, address=address, phone=phone)
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
                return JsonResponse({'success': True, 'message': 'Successfully Registered'})
        else:
            return JsonResponse({'success': False, 'message': 'Password and Confirm Password does not match'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
def kyc(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        fullname = data.get('fullname')
        address = data.get('address')
        phone = data.get('phone')
        dob = data.get('dob')
        gender = data.get('gender')
        profile = data.get('profile')
        landownership = data.get('landownership')
        citizen_front = data.get('citizen-front')
        citizen_back = data.get('citizen-back')
        res = farmer.objects.filter(id=id)

        # update data where the id is equal to the id


@csrf_exempt
def display_kyc(request):
    if request.method == 'GET':
        unverified_farmers = farmer.objects.filter(is_verified=False)
        serializer = farmerserializer(unverified_farmers, many=True)
        return JsonResponse(serializer.data, safe=False)
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

        response = cropdetail.objects.create(name=name, region=region, province=province, temperature=temperature,
                                             climate=climate, soil=soil, rain=rain, disease=disease, nutrient=nutrient)
        response.save()
        return JsonResponse({'sucess': True, 'message': 'Successfully Added'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        date = data.get('date')
        time = data.get('time')
        description = data.get('description')
        response = event.objects.create(
            name=name, date=date, time=time, description=description)
        response.save()
        return JsonResponse({'sucess': True, 'message': 'Successfully Added'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})


@api_view(['GET'])
def get_event(request):
    even = event.objects.all()
    serializer = eventserializer(even, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cropsdetail(request):  # get request from the frontend
    crops = cropdetail.objects.all()  # get all the data from the database
    serializer = cropdetailserializer(crops, many=True)
    return Response(serializer.data)  # return the data to the frontend


@csrf_exempt
@api_view(['Get'])
def get_seller_data(request):
    data = seller.objects.all()
    serializer = sellerserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['Get'])
def get_farmer_data(request):
    data = farmer.objects.all()
    serializer = farmerserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)



@csrf_exempt
@renderer_classes([JSONRenderer])
def forget(request):
    print("Inside forget")
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if email:
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
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})

        else:
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})

    return JsonResponse({'success': True, 'message': 'Password changed successfully'})
