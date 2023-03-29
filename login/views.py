from django.contrib.auth import login
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
        print(f'Email: {email}, Password: {password}')
        # user = authenticate(request, username=email, password=password)
        user = customauthenticate(email=email, password=password)
        print(user)
        if user is not None:
            print("Login successful")
            
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    
@csrf_exempt
def add_user(request):
    if request.method =='POST':
        data=json.loads(request.body)
        name=data.get('name')
        email = data.get('email')
        password=data.get('pass')
        address=data.get('address')
        phone=data .get('phone')
        user=data.get('user')
        print(f'Name: {name}, Email: {email}, Password: {password}, Address: {address}, Phone: {phone}, User: {user}')
        

@api_view(['GET'])
def cropsdetail(request):
    crops=cropdetail.objects.all()
    serializer=cropdetailserializer(crops,many=True)
    print(request,"request")
    return Response(serializer.data)

@csrf_exempt
def customauthenticate(email,password):
        print("Inside customauthenticate")
        print(f'Email: {email}, Password: {password}')
        try:
            data=login.objects.get(email=email,password=password)
            print('from userdb',data)
            return data
        except:
            return None
