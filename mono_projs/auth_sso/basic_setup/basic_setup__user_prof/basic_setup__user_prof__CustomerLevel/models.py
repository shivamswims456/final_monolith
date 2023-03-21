from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

um = get_user_model()

class user_models(models.Model):
    """
        userDependent model

    """

    user_name = models.CharField(max_length=60)
    Isonline = models.BooleanField()
    street = models.TextField(max_length=150)
    mobile = PhoneNumberField()
    dob = models.DateField()
    status = models.ForeignKey('basic_setup__user_prof.user_statues', on_delete=models.SET_NULL, null=True)
    
    country = models.ForeignKey('basic_setup.countries', on_delete=models.SET_NULL, null=True)
    time_zone = models.ForeignKey('basic_setup.time_zones', on_delete=models.SET_NULL, null=True)
    date_time_format = models.ForeignKey('basic_setup.date_time_format', on_delete=models.SET_NULL, null=True)
    currency = models.ForeignKey('basic_setup.currency', on_delete=models.SET_NULL, null=True) 
    state = models.ForeignKey('basic_setup.state', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('basic_setup.city', on_delete=models.SET_NULL, null=True)
    zip = models.ForeignKey('basic_setup.zip', on_delete=models.SET_NULL, null=True)
    
    created_by = models.ForeignKey(um, on_delete=models.SET_NULL, null=True, related_name='user_created_by')
    updated_by = models.ForeignKey(um, on_delete=models.SET_NULL, null=True, related_name='user_updated_by')
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)


    def confirm_chlds(self, obj, checkObj):

        #obj = country
        #checkObj = currency

        return obj.__class__.objects.filter(_chlds_included__id__exact = checkObj.id, enabled=True).exists()

    
    def save(self) -> None:

        testPairs = [
            (self.country, self.currency),
            (self.country, self.time_zone),
            (self.currency, self.state),
            (self.state, self.city),
            (self.city, self.zip)
        ]

        for pair in testPairs:
            
            if not self.confirm_chlds(*pair):

                raise ValueError(f'{pair[0]} not a valid attribute for {pair[0]}')

        


        return super().save()
    
