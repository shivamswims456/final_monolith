from django.apps import AppConfig


class SetupBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'setup_base'
