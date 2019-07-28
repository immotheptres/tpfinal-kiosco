from django.contrib import admin
from .models import proovedor
from .models import stock_entrada
from .models import stock_salida
from .models import Almacen


# Register your models here.
admin.site.register(proovedor)
admin.site.register(stock_entrada)
admin.site.register(stock_salida)
admin.site.register(Almacen)