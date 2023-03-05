from django.apps import AppConfig
from django.db.models.signals import post_migrate
from dynamic_tables.signals import replicated_slaves



class OrganisationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'organisations'

    
    def ready(self):

        post_migrate.connect(replicated_slaves, sender=self)