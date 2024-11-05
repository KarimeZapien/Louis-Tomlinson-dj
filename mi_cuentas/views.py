
from django.shortcuts import render

def login(request):
    return render(request, 'mi_cuentas/login.html')  # Asegúrate de que la plantilla existe
