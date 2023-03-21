from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
""" 

"organization_id": "10234695",

#admin
"name": "Zillum",
"contact_name": "John Smith",
"email": "johnsmith@zillum.com",
"language_code": "en",
"fiscal_year_start_month": 0,
"account_created_date": "2016-02-18",
"time_zone": "PST",
"is_org_active": true,


#currency
"currency": "Indian Rupee",
"currency_id": "460000000000097",
"currency_code": "USD",
"currency_symbol": "$",
"currency_format": "###,##0.00",
"price_precision": 2


#geoRegistered
"city": "Chennai",
"country": "India",
"description": "This is a sample description.",
"translation_enabled": true,
"street": "GST Road",
"state": "Tamil Nadu",
"employee_count": "100",
"zip": "603202",
"country_code": "IN",

"website": "https://www.zylker.com/",
"mobile": "0909090909",
"time_zone": "Asia/Calcutta",
"primary_email": "patricia.b@zohocorp.com",


 """

from django.contrib.auth import get_user_model


um = get_user_model()

class orgBasic(models.Model):

    organization_id = models.PositiveBigIntegerField()
    company_name = models.CharField(max_length=100)
    admin = models.ForeignKey(um, on_delete=models.SET_NULL, null=True)
    language_code = models.CharField(max_length=12)
    account_created_date = models.DateTimeField(auto_created=True)
    time_zone = models.CharField(max_length=100)
    is_org_active = models.BooleanField()
    #currency = models.
    price_precision = models.SmallIntegerField()
    address = models.TextField(max_length=300)
    #geoMod #geoMod
    #photo
    description = models.TextField(max_length=300)
    employee_count = models.PositiveIntegerField()
    website = models.URLField()
    primary_email = models.EmailField()
    mobile = PhoneNumberField()
    
    


