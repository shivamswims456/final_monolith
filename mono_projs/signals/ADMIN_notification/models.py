from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
# Create your models here.

um = get_user_model()


class individual_layer_stack(models.Model):

    """
        
        this model will narrate connection group to a new channel
        on being connected to which predecessor group it has to connect

    """

    user = models.ForeignKey(um, on_delete=models.CASCADE)
    channel_group = models.TextField(max_length=12)


    def __str__(self) -> str:
        return f'{self.channel_group}[{self.user}]'

        