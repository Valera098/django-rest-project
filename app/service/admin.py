from django.contrib import admin
from service.models import Order
from import_export import resources
from import_export.admin import ExportMixin, ImportExportModelAdmin

@admin.action(description="Change status to verified")
def change_status_true(selfmodeladmin, request, queryset):
    queryset.update(status=True)

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource
    actions = [change_status_true]
