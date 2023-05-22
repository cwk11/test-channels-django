from django.apps import AppConfig
from health_check.plugins import plugin_dir



class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

class MyAppConfig(AppConfig):
    name = 'my_app'

    def ready(self):
        from .backends import MyHealthCheckBackend
        plugin_dir.register(MyHealthCheckBackend)
