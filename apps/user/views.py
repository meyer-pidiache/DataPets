from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


@login_required(login_url='/')
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
            return redirect('/#login_section')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Nombre de usuario ya está en uso')
            return redirect('/#login_section')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Correo ya está en uso')
            return redirect('/#login_section')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('user:user')
    else:
        return render(request, 'main/index.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user:user')
        else:
            messages.info(request, 'Nombre de usuario o contraseña inválido')
            return redirect('/#login_section')
    else:
        return render(request, 'main/index.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Recuperación de contraseña'
                    email_template_name = 'user/forgot_password_message.txt'
                    parameters = {
                        'username': user.username,
                        'email': user.email,
                        'domain': 'datapets.pythonanywhere.com',
                        'site_name': 'DataPets',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, '', [user.email], fail_silently=False)
                    except:
                        return HttpResponse('Header inválido')
                    return redirect('user:password_reset_done')
            else:
                return redirect('main:home')
    else:
        password_form = PasswordResetForm()
    context = {
        'title': 'Restablecer contraseña',
        'password_form': password_form,
    }
    return render(request, 'user/password_reset.html', context)