from django.db import models




class countries(models.Model):

    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('basic_setup.currency', blank=True)
    

    def __str__(self):

        return self.name




class time_zones(models.Model):

    name = models.CharField(max_length=100)
    time_diff_min = models.FloatField(default=0)
    difference = models.CharField(max_length=100, default="", blank=True, null=True)
    _chlds_included = models.ManyToManyField('basic_setup.state', blank=True)
    

    def __str__(self):

        return f"{self.name} [{self.difference}]"
    

    def save(self):

        #convert to human readable time

        sign = "+ " if self.time_diff_min >= 0 else "-"  

        self.difference = f"{sign}{int((self.time_diff_min - self.time_diff_min%60) /60)}:{int(self.time_diff_min%60)}"
        
        super().save()





class currency(models.Model):

    name = models.CharField(max_length=100)
    currency_numeric_code = models.CharField(max_length=10)
    currency_short_code = models.CharField(max_length=3)
    price_precision = models.SmallIntegerField()
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('basic_setup.state', blank=True)
    

    def __str__(self):
         
        return self.name
     

class state(models.Model):

    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('basic_setup.city', blank=True)
    

    def __str__(self):

        return self.name
    

class city(models.Model):

    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    _chlds_included = models.ManyToManyField('basic_setup.zip', blank=True)
    

    def __str__(self):

        return self.name
        

class zip(models.Model):

    name = models.CharField(max_length=12)
    area_allocated = models.CharField(max_length=100)
    enabled = models.BooleanField()
    

    def __str__(self):

        return self.name
        


class date_time_format(models.Model):

    formats = models.CharField(max_length=30)   

    def __str__(self) -> str:
        return self.formats
