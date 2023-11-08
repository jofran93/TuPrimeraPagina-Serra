from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_de_inicio, name='pagina_de_inicio'),
    path('crear_cliente/', views.crear_cliente, name='cliente'),
    path('crear_producto/', views.crear_producto, name='producto'),
    path('crear_empleado/', views.crear_empleado, name='empleado')
]
