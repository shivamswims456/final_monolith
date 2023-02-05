from django.apps import AppConfig


class EcomUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ECOM_users'

    def ready(self) -> None:
        import ECOM_users.signals