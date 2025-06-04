from django.contrib import admin
from .models import Restaurante
from .models import Cliente
from .models import Mesa
from .models import Reserva


admin.site.register(Restaurante)
admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(Reserva)