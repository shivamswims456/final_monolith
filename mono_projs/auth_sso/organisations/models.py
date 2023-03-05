from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from datetime import datetime
from modification_logs.models import modification_logs as ml

# Create your models here.

um = get_user_model()



class FR_countries_allowed(models.Model):
   
   name = models.CharField(max_length=50)
   iso_code = models.CharField(max_length=15)
   country_code = models.CharField(max_length=5)
   
class FR_states_allowed(models.Model):
   
   country = models.ForeignKey(FR_countries_allowed, on_delete=models.CASCADE)
   name = models.CharField(max_length=70)

class FR_cities_allowed(models.Model):
   
   country = models.ForeignKey(FR_countries_allowed, on_delete=models.CASCADE)
   state = models.ForeignKey(FR_states_allowed, on_delete=models.CASCADE)
   name = models.CharField(max_length=70)

class FR_currencies_allowed(models.Model):
   
   country = models.ForeignKey(FR_countries_allowed, on_delete=models.CASCADE)
   name = models.CharField(max_length=30)
   symbol = models.CharField(max_length=3)

class FR_timezones_allowed(models.Model):
   
   name = models.TextField(max_length=70)

class F_organisation(models.Model):
 
   company_name = models.CharField(max_length=50)
   org_admin = models.ForeignKey(um, on_delete=models.SET_NULL, null=True)
   alias = models.CharField(max_length=50)
   country = models.ForeignKey(FR_countries_allowed, on_delete=models.CASCADE)
   zip = models.CharField(max_length=30)
   state = models.ForeignKey(FR_states_allowed, on_delete=models.CASCADE)
   city = models.ForeignKey(FR_cities_allowed, on_delete=models.CASCADE)
   street =  models.TextField(max_length=50)
   time_zone = models.ForeignKey(FR_timezones_allowed, on_delete=models.SET_NULL, null=True)
   description =  models.TextField(max_length=150)
   mc_status = models.BooleanField(default=False)
   domain_name = models.CharField(max_length=30)
   currency = models.ForeignKey(FR_currencies_allowed, on_delete=models.SET_NULL, null=True)
   employee_count = models.PositiveIntegerField(default=5)
   website = models.URLField()
   mobile = PhoneNumberField()
   phone = PhoneNumberField()
   primary_email = models.EmailField()
   modification_log = models.ManyToManyField(ml)    

class I_organisations_users(models.Model):

   user = models.ForeignKey(um, on_delete=models.CASCADE)
   organisations = models.ManyToManyField(F_organisation)
   modification_log = models.ManyToManyField(ml)

