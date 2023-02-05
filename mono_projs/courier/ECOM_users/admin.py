from django.contrib import admin
from ECOM_users import models
# Register your models here.

admin.site.register(models.ECOM_super_vendors)
admin.site.register(models.ECOM_vendors)
admin.site.register(models.ECOM_registers)
admin.site.register(models.ECOM_model_register)
admin.site.register(models.user_addition_instruction)