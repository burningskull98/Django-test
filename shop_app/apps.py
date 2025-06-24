"""
Этот модуль отвечает за конфигурацию приложений в проекте.
"""
from django.apps import AppConfig


class ShopAppConfig(AppConfig):
    """
     Конфигурация приложения для интернет-магазина.
     """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop_app'
