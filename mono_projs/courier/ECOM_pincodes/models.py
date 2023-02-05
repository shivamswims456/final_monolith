from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

um = get_user_model()
class ECOM_pincodes(models.Model):

    """
        #DO_NOT change model name statically related to multiModel(models)
        #If necesesarry please chage ECOM_register entry first
         
        
    """

    item_unique = models.CharField(max_length=100, unique=True)
    #DO_NOT change statically referenced in bulk import helpers
     
    status = models.TextField(max_length=30)#": 1,
    city_type = models.TextField(max_length=12, null=True, blank=True)#": "",
    pincode = models.TextField(max_length=6)#": 124103,
    active = models.BooleanField()#": true,
    state_code = models.TextField(max_length=6)#": "DL",
    city = models.TextField(max_length=40)#": "GURUGRAM",
    dccode = models.TextField(max_length=40)#": "GGA",
    route = models.TextField(max_length=100)#": "HR/I1H/JJR",
    state = models.TextField(max_length=100)#": "New Delhi",
    date_of_discontinuance = models.DateField(null=True, blank=True)#": "",
    city_code = models.TextField(max_length=12)#": "NEW"
    

