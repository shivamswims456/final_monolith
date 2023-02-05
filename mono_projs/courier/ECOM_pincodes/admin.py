from django.contrib import admin
from django.contrib.auth.models import Permission

class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    
admin.site.register(Permission, PermissionAdmin)
# Register your models here.
