from django.apps import AppConfig


class QAndAConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'q_and_a'

    def ready(self):
        import q_and_a.signals
