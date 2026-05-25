from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del producto',
                'class': 'form-input',
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción del producto...',
                'class': 'form-input',
                'rows': 3,
            }),
            'precio': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'form-input',
                'step': '0.01',
                'min': '0',
            }),
            'stock': forms.NumberInput(attrs={
                'placeholder': '0',
                'class': 'form-input',
                'min': '0',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-input',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio (COP)',
            'stock': 'Stock',
            'categoria': 'Categoría',
            'activo': 'Producto activo',
        }
