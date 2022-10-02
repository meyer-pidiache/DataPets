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
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import ReviewForm, UserUpdateForm, ProfileUpdateForm

@login_required(login_url='/')
def user_profile(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit = False)
            review.user = request.user
            review.save()
            form = ReviewForm()
            messages.success(request, '¡Tu reseña ha sido agregada!')
            return redirect('main:home')
        else:
            messages.error(request, 'Comentario inválido')
            return redirect('main:home')
    context = {'form': form}
    return render(request, 'user/user.html', context)

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            password = password1
        else:
            messages.warning(request, 'Las contraseñas no coinciden')
            return redirect('/#login_section')

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Nombre de usuario ya está en uso')
            return redirect('/#login_section')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Correo ya está en uso')
            return redirect('/#login_section')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            subject = 'Confirmación de correo electrónico'
            email_template_name = 'user/validation/email.txt'
            parameters = {
                'username': username,
                'email': email,
                'domain': 'datapets.herokuapp.com',
                'site_name': 'DataPets',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'protocol': 'https',
            }
            email_body = render_to_string(email_template_name, parameters)
            try:
                send_mail(subject, email_body, '', [email], fail_silently=False)
            except:
                return HttpResponse('Header inválido')
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
            messages.error(request, 'Nombre de usuario o contraseña inválido')
            return redirect('/#login_section')
    else:
        return render(request, 'main/index.html')

@login_required(login_url='/')
def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect('/')

@login_required(login_url='/')
def update_user(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu cuenta ha sido actualizada!')
            return redirect('user:user')
        else:
            messages.success(request, 'Datos inválidos')
            return redirect('user:update_user')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user/update_user.html', context)

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Recuperación de contraseña'
                    email_template_name = 'user/password_reset/forgot_password_message.txt'
                    parameters = {
                        'username': user.username,
                        'email': user.email,
                        'domain': 'datapets.herokuapp.com',
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
        'password_form': password_form,
    }
    return render(request, 'user/password_reset/password_reset.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.profile.is_editor = True
        user.save()
        messages.success(request, '¡Tu correo ha sido verificado!')
        return redirect('main:home')
    else:
        return HttpResponse('¡Link de activación inválido!')