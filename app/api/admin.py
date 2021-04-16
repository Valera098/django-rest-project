from django.contrib import admin
from api.models import Resort, Country, Tour
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResortResource(resources.ModelResource):
    class Meta:
        model = Resort
@admin.register(Resort)
class ResortAdmin(ImportExportModelAdmin):
    resource_class = ResortResource

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = Country

class TourResource(resources.ModelResource):
    class Meta:
        model = Tour
@admin.register(Tour)
class TourAdmin(ImportExportModelAdmin):
    resource_class = Tour

