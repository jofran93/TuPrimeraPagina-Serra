from django import forms # importacion de forms
from .models import cliente # importacion de modelo cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'apellido', 'edad', 'dni', 'telefono', 'correo']

from .models import productos # importacion de modelo producto

class ProductosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ['SKU', 'Precio']

from .models import empleados

class EmpleadosForm(forms.ModelForm): # importacion de modelo empleados
    class Meta:
        model = empleados
        fields = ['nombre', 'apellido', 'workId']
