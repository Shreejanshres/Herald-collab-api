from django.db import models

# Create your models here.
    
class user_farmer(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=50,blank=True,null=True)
    phone=models.CharField(max_length=11,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=50,unique=True,blank=True,null=True)
    password=models.CharField(max_length=50,blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True,null=True)
    dob=models.CharField(max_length=10,blank=True,null=True)
    citizenshipfrontpic=models.ImageField(upload_to='images/',blank=True,null=True)
    citizenshipbackpic=models.ImageField(upload_to='images/',blank=True,null=True)
    profilepic=models.ImageField(upload_to='images/',blank=True,null=True)
    landownerpic=models.ImageField(upload_to='images/',blank=True,null=True)

    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class user_seller(models.Model):
    id=models.AutoField(primary_key=True)
    company=models.CharField(max_length=50,blank=True,null=True)
    owner=models.CharField(max_length=50,blank=True,null=True)
    phone=models.CharField(max_length=11,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=50,unique=True,blank=True,null=True)
    password=models.CharField(max_length=50,blank=True,null=True)
    companyregpic=models.ImageField(upload_to='images/',blank=True,null=True)
    profilepic=models.ImageField(upload_to='images/',blank=True,null=True)

    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
   
class cropdetail(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    region=models.CharField(max_length=100)
    province=models.CharField(max_length=50,blank=True,null=True)
    temperature=models.CharField(max_length=50)
    climate=models.CharField(max_length=100)
    soil=models.CharField(max_length=100)
    rain=models.CharField(max_length=50)
    disease=models.CharField(max_length=100)
    nutrient=models.CharField(max_length=100)

    def  __str__(self):
        return self.name

    
