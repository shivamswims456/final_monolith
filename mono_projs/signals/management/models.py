from django.db import models
from uuid import uuid4
# Create your models here.





class application_setup(models.Model):

    application_name = models.CharField(max_length=50)
    application_key = models.UUIDField(default=uuid4)
    enabled = models.BooleanField()


    def __str__(self) -> str:

        return self.application_name


