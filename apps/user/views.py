from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def user(request):
    return render(request, 'user/user.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            password = password1
        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect('/')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Nombre de usuario ya está en uso')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Correo ya está en uso')
            return redirect('/')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('user/')
    else:
        return render(request, '/')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user/')
        else:
            messages.info(request, 'Nombre de usuario o contraseña inválido')
            return redirect('/')
    else:
        return render(request, '/')

def logout_user(request):
    auth.logout(request)
    return redirect('/')
