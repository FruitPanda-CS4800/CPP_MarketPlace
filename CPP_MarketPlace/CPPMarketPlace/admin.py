from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models
from Messaging import models as messageModels

# Register your models here.

#Add import and export functionality in admin page for Product database table
class Products(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(models.Product, Products)

admin.site.register(messageModels.ChatMessage)

admin.site.register(messageModels.Thread)