from django.contrib import admin
from django.urls import path, include
from EQBackend.EQapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djoser/', include('djoser.urls')),
    path('djoser/', include('djoser.urls.jwt')),
    path('register', views.signup),
    path('auth', views.get_token),
    path('tests/<int:pk>', views.TestView.as_view({'get': 'list', 'post': 'list'}))
    #path('tests/<int:pk>', views.test_endpoint)
]
