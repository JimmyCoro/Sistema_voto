from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from voto.models import Voto

# Create your views here.
def inicio_login(request):
    if request.method == 'POST':
        user_cedula = request.POST['cedula']
        user_pass = request.POST['password']
        errors = 'Usuario y contraseña incorrectos'

        usuario = authenticate(username = user_cedula, password = user_pass)
        realizo_voto = Voto.objects.filter(estudiante__user_id=usuario.id).count()
        
    
        if usuario and realizo_voto==0:
            login(request, usuario)
            return redirect('listas')
        
        else:
            messages.error(request,  errors)
            return redirect('inicio_login')
    else:
        print(request.GET)
        return render(request, 'estudiante/inicio_login.html',{})

