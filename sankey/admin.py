from __future__ import unicode_literals
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportMixin, ExportMixin
from import_export import resources, widgets, fields
from .models import DataPoint

class DataAdminResource(resources.ModelResource):

    class Meta(object):
        model = DataPoint

class DataAdmin(ImportExportModelAdmin):
    resource_class = DataAdminResource
    list_display = ('element','category','bool_val', 'element_description')
    search_fields = ['element','category','bool_val', 'element_description']


admin.site.register(DataPoint, DataAdmin)

# Register your models here.
