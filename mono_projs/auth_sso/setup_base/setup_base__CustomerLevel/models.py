from django.db import models

# Create your models here.


class geoCombination(models.Model):

    country = models.ForeignKey('setup_base.countries', on_delete=models.SET_NULL, null=True)
    currency = models.ForeignKey('setup_base.currency', on_delete=models.SET_NULL, null=True) 
    state = models.ForeignKey('setup_base.state', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('setup_base.city', on_delete=models.SET_NULL, null=True)
    zip = models.ForeignKey('setup_base.zip', on_delete=models.SET_NULL, null=True)
    

    def confirm_chlds(self, obj, checkObj):

        #obj = country
        #checkObj = currency

        return obj.objects.filter(_chlds_included__id__exact = checkObj.id, enabled=True).exists()

    

    def clean(self) -> None:

        testPairs = [
            (self.country, self.currency),
            (self.currency, self.state),
            (self.state, self.city),
            (self.city, self.zip)
        ]

        for pair in testPairs:
            
            if not self.confirm_chlds(*pair):

                raise ValueError(f'{pair[0]} not a valid attribute for {pair[0]}')

            #start here

            
        return super().clean()
