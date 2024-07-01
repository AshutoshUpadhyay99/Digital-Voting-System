from django.apps import AppConfig


class VotingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'voting_app'


class MyAppConfig(AppConfig):
    name = 'voting_app'

    def ready(self):
        # Import and register the custom filter
        from . import custom_filters
