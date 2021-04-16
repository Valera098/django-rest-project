from django.contrib import admin
from service.models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
