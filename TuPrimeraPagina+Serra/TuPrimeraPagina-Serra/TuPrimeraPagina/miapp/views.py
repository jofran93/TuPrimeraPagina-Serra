# Create your views here.
from .forms import ClienteForm, ProductoForm, EmpleadoForm
from .models import Cliente, Producto, Empleado


from django.shortcuts import render,redirect

def pagina_de_inicio(request):
    return render(request, 'template.html')


def crear_cliente(request):
    if request.method == 'POST':
        form1 = ClienteForm(request.POST)
        if form1.is_valid():
            Cliente = form1.save()
            return redirect("cliente")
    else:
        form1 = ClienteForm()
        return render(request, 'subpaginas/cliente.html', {'form1':form1})



def crear_producto(request):
    if request.method == 'POST':
        form2 = ProductoForm(request.POST)
        if form2.is_valid():
            Producto = form2.save()
            return redirect('producto')
        
    else:
        form2 = ProductoForm()
        return render(request, 'subpaginas/producto.html', {'form2': form2})

def crear_empleado(request):
    if request.method == 'POST':
        form3 = EmpleadoForm(request.POST)
        if form3.is_valid():
            Empleado = form3.save()
            return redirect('empleado')
        
    else:
        form3 = EmpleadoForm()
        return render(request, 'subpaginas/empleado.html', {'form3': form3})
