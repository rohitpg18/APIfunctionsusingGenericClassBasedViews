from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from api.models import *

class StudentImportExport(ImportExportModelAdmin):
    pass


class StudentAdmin (admin.ModelAdmin):
    list_display = ['name', 'phone_number' , 'email']


admin.site.register(Student , StudentImportExport)
