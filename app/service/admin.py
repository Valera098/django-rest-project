from django.contrib import admin
from service.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
