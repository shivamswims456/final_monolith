from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Create your models here.
user_model = get_user_model()




class user_addition_instruction(models.Model):
    """ 
        user_addition_instruction = user_instrucntions
    """
    name = models.CharField(max_length=50, unique=True)
    instruction = models.JSONField()
    remove_instructions = models.JSONField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, unique=True)


    def __str__(self) -> str:
        return self.name 








class ECOM_registers(models.Model):

    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self) -> str:
        return self.name
    




class ECOM_model_register(models.Model):

    name = models.CharField(max_length=150, unique=True)
    register = models.ForeignKey(ECOM_registers, on_delete=models.CASCADE)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name    




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