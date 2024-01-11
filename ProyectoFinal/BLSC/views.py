from django.shortcuts import render
from .forms import UserCreationFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth import login, authenticate
from . import models
from .models import Obra, Comentario
from django.urls import reverse_lazy


##### HOME (INICIO):

def home_view(request):
    return render(request, "BLSC/home.html")


def acercademi_view(request):
    return render(request, "BLSC/acercademi.html")

##### SIGN IN, LOGIN Y LOGOUT:

def signin_view(request):

    if request.method == "GET":
        return render(
            request,
            "BLSC/signin.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "BLSC/home.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "BLSC/login.html",
                {"form": formulario}
            )
        



def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            "BLSC/home.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
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
            password = informacion ["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "BLSC/home.html",
                {"mensaje": f"Bienvenidx {modelo.username}"}
            )
        else:
            return render(
                request,
                "BLSC/login.html",
                {"form": formulario}
            )


####VIEWS PARA OBRAS:
        
def blogpages_view(request):
    obras = models.Obra.objects.all()
    context = {"blogpages":obras}
    return render(request, "BLSC/blog_pages.html", context)


def lista_poesias_view(request):
    poesias = Obra.objects.filter(tipo="poesia")

    return render(request, 'lista_poesias.html', {'poesias': poesias})


class PoesiaLista(LoginRequiredMixin, ListView):
    context_object_name = 'poesias'
    queryset = Obra.objects.filter(tipo__startswith='poesía')
    template_name = 'BLSC/lista_poesias.html'
    login_url = '/login/'

class PoesiaDetalle(LoginRequiredMixin, DetailView):
    model = Obra
    context_object_name = 'poesia'
    template_name = 'BLSC/poesia_detalle.html'

#class PoesiaUpdate(LoginRequiredMixin, UpdateView):
#    model = Obra
#    form_class = ActualizacionObra
#    success_url = reverse_lazy('poesias')
#    context_object_name = 'poesia'
#    template_name = 'BLSC/poesia_edicion.html'

#class GuitarraDelete(LoginRequiredMixin, DeleteView):
#    model = Obra
#    success_url = reverse_lazy('poesias')
#    context_object_name = 'poesia'
#    template_name = 'Base/guitarraBorrado.html'
