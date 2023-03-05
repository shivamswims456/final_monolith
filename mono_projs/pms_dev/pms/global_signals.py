from django.db.models.signals import post_migrate

def replicate_slaves(sender, instance, created, **kwargs):
    print("+++++++++++++++++++++++++++++++++++++")
    print(sender, instance, created, **kwargs)