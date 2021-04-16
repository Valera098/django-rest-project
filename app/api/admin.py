from django.contrib import admin
from api.models import *

@admin.register(Resort)
class ResortAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass
