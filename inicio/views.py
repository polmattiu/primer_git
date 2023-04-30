from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView 
from django.contrib.auth.mixins import LoginRequiredMixin


from inicio.models import Gasto

def inicio(request):
    return render(request, 'inicio/inicio.html')

def sobre_mi(request):
    return render(request, 'inicio/sobre_mi.html')


class GastoListView(ListView):
    model = Gasto
    template_name = "inicio/lista_de_gastos.html"



class GastoDetailView(DetailView):
    model = Gasto
    template_name = "inicio/detalle_gasto.html"


class GastoCreateView(CreateView):
    model = Gasto
    template_name = "inicio/crear_gasto.html"
    fields = ['tipo','articulo','descripcion','stock','fecha_de_carga','precio', 'imagen']
    success_url = '/gastos/'



class GastoUpdateView(LoginRequiredMixin, UpdateView):
    model = Gasto
    template_name = "inicio/modificar_gasto.html"
    fields = ['tipo','articulo','descripcion','stock','fecha_de_carga','precio','imagen']
    success_url = '/gastos/'


class GastoDeleteView(LoginRequiredMixin, DeleteView):
    model = Gasto
    template_name = "inicio/eliminar_gasto.html"
    success_url = '/gastos/'


