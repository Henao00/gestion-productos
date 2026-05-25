from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Sum
from .models import Producto
from .forms import ProductoForm


# ─── HOME ────────────────────────────────────────────────────────────────────
def home(request):
    total_productos = Producto.objects.count()
    total_activos   = Producto.objects.filter(activo=True).count()
    valor_inventario = Producto.objects.aggregate(
        total=Sum('precio')
    )['total'] or 0
    ultimos = Producto.objects.filter(activo=True)[:4]

    context = {
        'total_productos':  total_productos,
        'total_activos':    total_activos,
        'valor_inventario': valor_inventario,
        'ultimos':          ultimos,
    }
    return render(request, 'productos/home.html', context)


# ─── SOBRE NOSOTROS ──────────────────────────────────────────────────────────
def nosotros(request):
    return render(request, 'productos/nosotros.html')


# ─── LISTA DE PRODUCTOS ──────────────────────────────────────────────────────
def lista_productos(request):
    query     = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')

    productos = Producto.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    if categoria:
        productos = productos.filter(categoria=categoria)

    categorias       = Producto.CATEGORIA_CHOICES
    total_productos  = Producto.objects.count()
    total_activos    = Producto.objects.filter(activo=True).count()
    valor_inventario = Producto.objects.aggregate(
        total=Sum('precio')
    )['total'] or 0

    context = {
        'productos':            productos,
        'categorias':           categorias,
        'query':                query,
        'categoria_seleccionada': categoria,
        'total_productos':      total_productos,
        'total_activos':        total_activos,
        'valor_inventario':     valor_inventario,
    }
    return render(request, 'productos/lista.html', context)


# ─── CREAR PRODUCTO ──────────────────────────────────────────────────────────
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'✓ Producto "{producto.nombre}" registrado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'productos/form.html', {'form': form, 'titulo': 'Nuevo Producto'})


# ─── EDITAR PRODUCTO ─────────────────────────────────────────────────────────
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'✓ Producto "{producto.nombre}" actualizado.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/form.html', {
        'form':    form,
        'titulo':  'Editar Producto',
        'producto': producto,
    })


# ─── ELIMINAR PRODUCTO ───────────────────────────────────────────────────────
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'✓ Producto "{nombre}" eliminado.')
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminar.html', {'producto': producto})
