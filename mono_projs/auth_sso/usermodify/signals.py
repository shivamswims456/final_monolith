from django.db.models.signals import post_save
from random import randint
from django.contrib.auth import get_user_model
from django.dispatch import receiver


um = get_user_model()

@receiver(post_save, sender=um)
def update_username_with_unique_number(sender, instance, created, **kwargs):

    if created:
    
        while True:
            un = str(randint(1, 10000000000)).zfill(10)
            if not sender.objects.filter(username = un).exists():

                break
        
        instance.username = un
        instance.save()

