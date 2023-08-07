from django.contrib import admin
from django.urls import path, include
from EQBackend.EQapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.signup),
    path('auth', views.get_token),
    path('djoser/', include('djoser.urls')),
    path('djoser/', include('djoser.urls.jwt')),
]
