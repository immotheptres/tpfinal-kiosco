from django.shortcuts import render

# Create your views here.
def Almacen_list(request):
    return render(request, 'kiosco/Almacen_list.html', {})
