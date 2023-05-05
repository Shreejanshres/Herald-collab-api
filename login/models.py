from django.db import models

# Create your models here.


class farmer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profilepic = models.ImageField(
        upload_to='profilepic', blank=True, null=True)
    citizenship_front = models.ImageField(
        upload_to='citizenship_front', blank=True, null=True)
    citizenship_back = models.ImageField(
        upload_to='citizenship_back', blank=True, null=True)
    landownership = models.ImageField(
        upload_to='landownership', blank=True, null=True)
    is_verified = models.BooleanField(default=False)


class seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class cropdetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=50, blank=True, null=True)
    temperature = models.CharField(max_length=50)
    climate = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    rain = models.CharField(max_length=50)
    disease = models.CharField(max_length=100)
    nutrient = models.CharField(max_length=100)


class event(models.Model):
    eventname = models.CharField(max_length=50)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdescription = models.TextField()
