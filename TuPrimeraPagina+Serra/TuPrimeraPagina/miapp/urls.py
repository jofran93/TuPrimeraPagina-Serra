from django.urls import path
from . import views

urlpatterns = [
    # URLs Pagina de Inicio
    path('', views.pagina_de_inicio, name='pagina_de_inicio'),
    path('prueba/', views.pagina_de_prueba, name='pagina_de_prueba'),

    # URLs para Cliente
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),

    # URLs para Producto
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),

    # URLs para Empleado
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('lista_empleados/', views.lista_empleados, name='lista_empleados'),
]
