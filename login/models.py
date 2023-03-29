from django.db import models

# Create your models here.
class user_farmer(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    citizenshipfrontpic=models.ImageField(upload_to='images/')
    citizenshipbackpic=models.ImageField(upload_to='images/')
    profilepic=models.ImageField(upload_to='images/')
    landownerpic=models.ImageField(upload_to='images/')

    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

class user_seller(models.Model):
    id=models.AutoField(primary_key=True)
    company=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=100)
    companyregpic=models.ImageField(upload_to='images/')
    profilepic=models.ImageField(upload_to='images/')

    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

class login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    farmer_id=models.ForeignKey(user_farmer,on_delete=models.CASCADE,blank=True,null=True)
    seller_id=models.ForeignKey(user_seller,on_delete=models.CASCADE,blank=True,null=True)

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

    
