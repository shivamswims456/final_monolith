from django.db import models

# Create your models here.



class user_statues(models.Model):

    statues = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.statues