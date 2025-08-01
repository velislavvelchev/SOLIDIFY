from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SOLIDIFY.accounts'

    def ready(self):
        import SOLIDIFY.accounts.signals

