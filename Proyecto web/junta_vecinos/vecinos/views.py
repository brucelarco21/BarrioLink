from django.shortcuts import render, redirect
from .models import Vecino, Noticia

# Página de inicio
def home(request):
    return render(request, 'vecinos/home.html')

# Registro de vecinos
def registro_vecino(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']

        Vecino.objects.create(
            nombre=nombre,
            email=email,
            direccion=direccion,
            telefono=telefono
        )
        return redirect('home')
    return render(request, 'vecinos/registro.html')

# Solicitud de certificados
def certificados(request):
    if request.method == 'POST':
        mensaje = "Solicitud de certificado enviada con éxito."
        return render(request, 'vecinos/certificados.html', {'mensaje': mensaje})
    return render(request, 'vecinos/certificados.html')

# Noticias
def noticias(request):
    lista = Noticia.objects.all().order_by('-fecha')
    return render(request, 'vecinos/noticias.html', {'noticias': lista})
