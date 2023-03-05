from django.db import models

# Create your models here.


class dynamic_tables(models.Model):

    table_name = models.CharField(max_length=40, primary_key=True)
    proto_name = models.TextField(max_length=150)
