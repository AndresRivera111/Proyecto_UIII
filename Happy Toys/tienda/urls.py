from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_carrito, name='eliminar_carrito'),
]
