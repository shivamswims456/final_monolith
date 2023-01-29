from django.apps import AppConfig


class UsermodifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usermodify'

    def ready(self) -> None:
        import usermodify.signals
