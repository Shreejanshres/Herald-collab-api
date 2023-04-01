from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializer import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt   
def Login(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        password = data.get('pass')
        user=data.get('user')
        print(f'Email: {email}, Password: {password}')
        user = customauthenticate(email=email, password=password,user=user)
        print(user)
        if user is not None:
            print("Login successful")
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    
@csrf_exempt
def customauthenticate(email,password,user):
        print("Inside customauthenticate")
        print(f'Email: {email}, Password: {password},user:{user}')
        if user=="farmer":
            try:
                data=user_farmer.objects.get(email=email,password=password)
                return data
            except:
                return None
        elif user=="seller":
            try:
                data=user_seller.objects.get(email=email,password=password)
                return data
            except:
                return None
 

@api_view(['GET'])
def cropsdetail(request):
    crops=cropdetail.objects.all()
    serializer=cropdetailserializer(crops,many=True)
    return Response(serializer.data)


        
@csrf_exempt
def add_user(request):
    print("Inside add_user")
    if request.method =='POST':
        data=json.loads(request.body)
        email = data.get('email')
        password=data.get('pass')
        user=data.get('user')
        print(f'Email: {email}, Password: {password}, User: {user}')
        if user=='farmer':
            try:
                data=user_farmer.objects.get(email=email)
                print(data)
                return JsonResponse({'success': False, 'message': 'User already exists'})
            except:
                data=user_farmer.objects.create(email=email,password=password)
                data.save()
                return JsonResponse({'success': True, 'message': 'User added successfully'})
        elif user=='seller':
            try:
                data=user_seller.objects.get(email=email)
                return JsonResponse({'success': False, 'message': 'User already exists'})
            except:
                data=user_seller.objects.create(email=email,password=password)
                data.save()
                return JsonResponse({'success': True, 'message': 'User added successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid user type'})
    else:
        return Response({'message': 'Invalid request method'})


@csrf_exempt
def kyc(request):
    print("Inside kyc")
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        name=data.get('name')
        phone=data.get('phone')
        address=data.get('address')
        gender=data.get('gender')
        dob=data.get('dob')
        print(name,email,phone,address,gender,dob)
        try:
            data=user_farmer.objects.get(email=email)
            data.fullname=name
            data.phone=phone
            data.address=address
            data.gender=gender
            data.dob=dob
            data.save()
            return JsonResponse({'success': True, 'message': 'KYC updated successfully'})
        except:
            return JsonResponse({'success': False, 'message': 'User does not exist'})
            
    else:
        return Response({'message': 'Invalid request method'})
    

@csrf_exempt
def forget(request):
    print("Inside forget")
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        password=data.get('password')
        print(email)
        try:
            data=user_farmer.objects.get(email=email)
            data.password=password
        except:
            return JsonResponse({'success': False, 'message': 'User does not exist'})
            
    else:
        return Response({'message': 'Invalid request method'})