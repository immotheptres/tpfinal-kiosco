from django.contrib import admin
from .models import proovedor
from .models import stock_engreso
from .models import stock_venta
from .models import Almacen


# Register your models here.
admin.site.register(proovedor)
admin.site.register(stock_engreso)
admin.site.register(stock_venta)
admin.site.register(Almacen)