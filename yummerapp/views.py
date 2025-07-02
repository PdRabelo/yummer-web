from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Restaurante, Mesa, Reserva

# Cliente views
class ClienteListView(ListView):
    model = Cliente
    template_name = 'yummerapp/cliente_list.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'yummerapp/cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'yummerapp/cliente_form.html'
    fields = ['nome', 'email', 'telefone']
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'yummerapp/cliente_form.html'
    fields = ['nome', 'email', 'telefone']
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'yummerapp/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

# Restaurante views
class RestauranteListView(ListView):
    model = Restaurante
    template_name = 'yummerapp/restaurante_list.html'
    context_object_name = 'restaurantes'

class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name = 'yummerapp/restaurante_detail.html'
    context_object_name = 'restaurante'

class RestauranteCreateView(CreateView):
    model = Restaurante
    template_name = 'yummerapp/restaurante_form.html'
    fields = ['nome', 'endereco', 'telefone']
    success_url = reverse_lazy('restaurante-list')

class RestauranteUpdateView(UpdateView):
    model = Restaurante
    template_name = 'yummerapp/restaurante_form.html'
    fields = ['nome', 'endereco', 'telefone']
    success_url = reverse_lazy('restaurante-list')

class RestauranteDeleteView(DeleteView):
    model = Restaurante
    template_name = 'yummerapp/restaurante_confirm_delete.html'
    success_url = reverse_lazy('restaurante-list')

# Mesa views
class MesaListView(ListView):
    model = Mesa
    template_name = 'yummerapp/mesa_list.html'
    context_object_name = 'mesas'

class MesaDetailView(DetailView):
    model = Mesa
    template_name = 'yummerapp/mesa_detail.html'
    context_object_name = 'mesa'

class MesaCreateView(CreateView):
    model = Mesa
    template_name = 'yummerapp/mesa_form.html'
    fields = ['restaurante', 'numero', 'capacidade']
    success_url = reverse_lazy('mesa-list')

class MesaUpdateView(UpdateView):
    model = Mesa
    template_name = 'yummerapp/mesa_form.html'
    fields = ['restaurante', 'numero', 'capacidade']
    success_url = reverse_lazy('mesa-list')

class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'yummerapp/mesa_confirm_delete.html'
    success_url = reverse_lazy('mesa-list')

# Reserva views
class ReservaListView(ListView):
    model = Reserva
    template_name = 'yummerapp/reserva_list.html'
    context_object_name = 'reservas'

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'yummerapp/reserva_detail.html'
    context_object_name = 'reserva'

class ReservaCreateView(CreateView):
    model = Reserva
    template_name = 'yummerapp/reserva_form.html'
    fields = ['cliente', 'mesa', 'data', 'hora_inicio', 'hora_fim', 'status']
    success_url = reverse_lazy('reserva-list')

class ReservaUpdateView(UpdateView):
    model = Reserva
    template_name = 'yummerapp/reserva_form.html'
    fields = ['cliente', 'mesa', 'data', 'hora_inicio', 'hora_fim', 'status']
    success_url = reverse_lazy('reserva-list')

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'yummerapp/reserva_confirm_delete.html'
    success_url = reverse_lazy('reserva-list')
