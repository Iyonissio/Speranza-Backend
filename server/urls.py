from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.views import CondutorView
from rest_framework import routers 

route = routers.DefaultRouter()
route.register("", CondutorView, basename="condutorview")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', include('products.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
