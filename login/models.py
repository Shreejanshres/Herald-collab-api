from django.db import models

# Create your models here.

class farmer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
  

class seller(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

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
    