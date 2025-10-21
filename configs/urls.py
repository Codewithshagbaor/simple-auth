from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(f"api/v1/auth/", include("base.urls")),
    path('admin/', admin.site.urls),
]