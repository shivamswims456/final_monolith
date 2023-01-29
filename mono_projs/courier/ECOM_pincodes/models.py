from django.db import models

# Create your models here.


class ECOM_pincodes(models.Model):

    status = models.TextField(max_length=30)#": 1,
    city_type = models.TextField(max_length=12)#": "",
    pincode = models.TextField(max_length=6)#": 124103,
    active = models.BooleanField()#": true,
    state_code = models.TextField(max_length=6)#": "DL",
    city = models.TextField(max_length=40)#": "GURUGRAM",
    dccode = models.TextField(max_length=40)#": "GGA",
    route = models.TextField(max_length=100)#": "HR/I1H/JJR",
    state = models.TextField(max_length=100)#": "New Delhi",
    date_of_discontinuance = models.DateField(null=True, blank=True)#": "",
    city_code = models.TextField(max_length=12)#": "NEW"
    master_vendor = models.TextField(max_length=130)# master vendor for which pincodes are being fetched


    