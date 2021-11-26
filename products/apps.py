from django.apps import AppConfig

#O nome da App Ficticia que ira rodar o beckend name = 'products'
class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
