from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "dare_rem_django_site"

    def ready(self):
        import_module("dare_rem_django_site.receivers")
