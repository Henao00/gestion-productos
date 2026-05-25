from django.urls import path
from . import views

urlpatterns = [
    # Páginas principales
    path('',           views.home,            name='home'),
    path('nosotros/',  views.nosotros,         name='nosotros'),
    path('productos/', views.lista_productos,  name='lista_productos'),
    path('nuevo/',     views.crear_producto,   name='crear_producto'),

    # CRUD
    path('editar/<int:pk>/',   views.editar_producto,   name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto,  name='eliminar_producto'),
]
