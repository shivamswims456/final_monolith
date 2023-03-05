from django.db import models

# Create your models here.


class good(models.Model):

    names = models.CharField(max_length=30)
    ert1 = models.DateTimeField(auto_now_add=True)
    jelo = models.PositiveBigIntegerField()    
    
    