from django.urls import path
from . import views

urlpatterns = [
    

    # Cliente URLs
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/deletar/', views.ClienteDeleteView.as_view(), name='cliente-delete'),

    # Restaurante URLs
    path('restaurantes/', views.RestauranteListView.as_view(), name='restaurante-list'),
    path('restaurantes/<int:pk>/', views.RestauranteDetailView.as_view(), name='restaurante-detail'),
    path('restaurantes/novo/', views.RestauranteCreateView.as_view(), name='restaurante-create'),
    path('restaurantes/<int:pk>/editar/', views.RestauranteUpdateView.as_view(), name='restaurante-update'),
    path('restaurantes/<int:pk>/deletar/', views.RestauranteDeleteView.as_view(), name='restaurante-delete'),

    # Mesa URLs
    path('mesas/', views.MesaListView.as_view(), name='mesa-list'),
    path('mesas/<int:pk>/', views.MesaDetailView.as_view(), name='mesa-detail'),
    path('mesas/novo/', views.MesaCreateView.as_view(), name='mesa-create'),
    path('mesas/<int:pk>/editar/', views.MesaUpdateView.as_view(), name='mesa-update'),
    path('mesas/<int:pk>/deletar/', views.MesaDeleteView.as_view(), name='mesa-delete'),

    # Reserva URLs
    path('reservas/', views.ReservaListView.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva-detail'),
    path('reservas/novo/', views.ReservaCreateView.as_view(), name='reserva-create'),
    path('reservas/<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='reserva-update'),
    path('reservas/<int:pk>/deletar/', views.ReservaDeleteView.as_view(), name='reserva-delete'),
]
