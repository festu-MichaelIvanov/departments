from django.contrib import admin
from django.urls import include, path

from app.urls import urlpatterns as departments_urls

urlpatterns = [
    path("departments/", include(departments_urls), name="departments"),
    path("admin/", admin.site.urls),
]
