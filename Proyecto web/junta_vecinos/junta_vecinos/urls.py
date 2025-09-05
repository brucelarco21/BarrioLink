from django.contrib import admin
from django.urls import path
from vecinos import views  # importamos las vistas de la app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro_vecino, name='registro'),
    path('certificados/', views.certificados, name='certificados'),
    path('noticias/', views.noticias, name='noticias'),
]
