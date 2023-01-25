from django.contrib import admin
from kv_report.models import kv_creds


# Register your models here.

@admin.register(kv_creds)
class kv_credsAdmin(admin.ModelAdmin):

    pass

