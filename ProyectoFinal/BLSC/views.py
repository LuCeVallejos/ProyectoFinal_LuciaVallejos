from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserEditionFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Avatar



##### HOME (INICIO):

def home_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""

    return render(request, "BLSC/home.html", context={"avatar_url": avatar_url})



##### ABOUT:
def acercademi_view(request):
    return render(request, "BLSC/acercademi.html")



##### SIGN IN, LOGIN Y LOGOUT:

def signin_view(request):
    if request.method == "GET":
        return render(
            request,
            "BLSC/signin.html",
            {"form": CustomUserCreationForm()}
        )
    else:
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            # Construir la URL con el mensaje como parámetro
            url_signinok = reverse('BLSC:signinok') + f'?mensaje=Usuarix creadx: {usuario}'
            return redirect(url_signinok)
        else:
            return render(
                request,
                "BLSC/signin.html",
                {"form": formulario}
            )



def signinok_view(request):
    mensaje = request.GET.get('mensaje', '')
    return render(request, "BLSC/signinok.html", {"mensaje": mensaje})



def login_view(request):
    # Verifica si el usuario ya está autenticado
    if request.user.is_authenticated:
        return render(
            request,
            "BLSC/signinok.html",
            {"mensaje": f"¡¡Hola, @{request.user.username}!! Estás logeadx y puedes interactuar libremente en nuestra página."}
        )

    if request.method == "GET":
        return render(
            request,
            "BLSC/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            # Redirige al usuario a la página de inicio
            return redirect('BLSC:home')
        else:
            return render(
                request,
                "BLSC/login.html",
                {"form": formulario}
            )



##### EDITAR PERFIL:

@login_required
def editarperfil_view(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""



    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "BLSC/editarperfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
        )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("BLSC:home")
