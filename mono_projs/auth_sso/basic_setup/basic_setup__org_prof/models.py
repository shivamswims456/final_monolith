from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from random import randint
# Create your models here.


um = get_user_model()


class org_model(models.Model):

    """
        userDependepdent model 
    """

    org_id = models.PositiveBigIntegerField(blank=True)
    company_name = models.CharField(max_length=120)#Zylker",
    admin_user = models.ForeignKey(um, on_delete=models.CASCADE)
    description = models.TextField(max_length=150)#This is a sample description.",
    street = models.TextField(max_length=150)#GST Road",
    alias = models.TextField(max_length=150)#sample alias",
    employee_count = models.PositiveIntegerField()#100",
    website = models.URLField()#https://www.zylker.com/",
    mobile = PhoneNumberField()#0909090909"
    primary_email = models.EmailField()#patricia.b@zohocorp.com",


    country = models.ForeignKey('basic_setup.countries', on_delete=models.SET_NULL, null=True)
    time_zone = models.ForeignKey('basic_setup.time_zones', on_delete=models.SET_NULL, null=True)
    currency = models.ForeignKey('basic_setup.currency', on_delete=models.SET_NULL, null=True) 
    state = models.ForeignKey('basic_setup.state', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('basic_setup.city', on_delete=models.SET_NULL, null=True)
    zip = models.ForeignKey('basic_setup.zip', on_delete=models.SET_NULL, null=True)
    

    
    created_by = models.ForeignKey(um, on_delete=models.SET_NULL, null=True, related_name='org_created_by')
    updated_by = models.ForeignKey(um, on_delete=models.SET_NULL, null=True, related_name='org_updated_by')
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)


    

    def __str__(self):

        return str(self.org_id)

    """
        low level data validation functions  
        and id allot functions
    """

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

        

        """
            assigning id to the object 
        """
        

        while True:

            un = str(randint(1, 10000000000)).zfill(10)
            if not org_model.objects.filter(org_id = un).exists():

                break
        
        self.org_id = un



        return super().save()


class org_users(models.Model):

    """
        userdependent model
        Model for holding relation of a org with all of its 
    """
    org = models.OneToOneField('basic_setup__org_prof.org_model', on_delete=models.CASCADE)
    users = models.ManyToManyField(um)

    def __str__(self) -> str:
        
        return str(self.org.org_id)