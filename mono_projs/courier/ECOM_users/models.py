from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user_model = get_user_model()

class ECOM_super_vendors(models.Model):

    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    ecom_user = models.CharField(max_length=150)
    ecom_password = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        
        return self.user.email


class ECOM_vendors(models.Model):

    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    wallet_balance = models.FloatField()



    def __str__(self) -> str:
        return self.user.username