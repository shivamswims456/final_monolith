from django.db import models

# Create your models here.
class zip(models.Model):

    data = models.CharField(max_length=30)