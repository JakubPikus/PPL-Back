from django.apps import AppConfig



class PpleloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pplelo'

    def ready(self):
        from faceitUpdater import update
        update.start()
