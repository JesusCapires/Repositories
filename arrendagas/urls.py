from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("propiedades/", include("propiedades.urls")),
    path("admin/", admin.site.urls),
]