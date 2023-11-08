from django.shortcuts import render, redirect
from .models import Cliente, Producto, Empleado
from .forms import ClienteForm, ProductoForm, EmpleadoForm

def pagina_de_inicio(request):
    return render(request, 'template.html')


def pagina_de_prueba(request):
    return render(request, 'prueba.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'subpaginas/crear_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'subpaginas/lista_clientes.html', {'clientes': clientes})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'subpaginas/crear_producto.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'subpaginas/lista_productos.html', {'productos': productos})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'subpaginas/crear_empleado.html', {'form': form})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'subpaginas/lista_empleados.html', {'empleados': empleados})


from django.shortcuts import render
from .models import Cliente