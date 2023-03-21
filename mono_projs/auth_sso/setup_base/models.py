from django.db import models






class countries(models.Model):

    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('setup_base.currency')



class currency(models.Model):

    currency_name = models.CharField(max_length=100)
    currency_numeric_code = models.CharField(max_length=10)
    currency_short_code = models.CharField(max_length=3)
    price_precision = models.SmallIntegerField()
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('setup_base.state')


class state(models.Model):

    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('setup_base.city')

class city(models.Model):

    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('setup_base.zip')


class zip(models.Model):

    name = models.CharField(max_length=12)
    area_allocated = models.CharField(max_length=100)
    enabled = models.BooleanField()


