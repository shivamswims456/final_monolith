from django.db.models.signals import post_migrate
from good.models import good
from django.dispatch import receiver

@receiver(post_migrate, sender=good)
def rec(*args, **kwargs):

    print(*args, **kwargs)