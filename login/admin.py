from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user_farmer)
admin.site.register(user_seller)
admin.site.register(login)
admin.site.register(cropdetail)

