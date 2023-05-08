from django.contrib.admin import site
from .models import *

# Register your models here.
site.register(seller)
site.register(farmer)
site.register(cropdetail)
site.register(event)
site.register(admin)
