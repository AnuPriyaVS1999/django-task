
from django.contrib import admin
from django.urls import path, include
from django.conf import setting
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include("web.urls", namespace="web")),
]+ static (settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)
