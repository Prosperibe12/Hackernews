from django.apps import AppConfig


class HnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hnapp'
    
    # def ready(self):
    #     from jobs import updater
    #     updater.start()
        
    # def ready(self):
    #     from jobs import updater
    #     updater.starts()

