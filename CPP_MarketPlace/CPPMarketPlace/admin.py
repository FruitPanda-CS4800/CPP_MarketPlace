from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models

# Register your models here.

#Add import and export functionality in admin page for Product database table
class Products(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(models.Product, Products)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')  # list of fields to display in the admin interface
# Register UserProfile with the admin site
admin.site.register(models.UserProfile, UserProfileAdmin)