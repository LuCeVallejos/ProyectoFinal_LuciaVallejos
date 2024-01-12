from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from BLSC.views import home_view
from .views import signin_view, signinok_view, login_view, acercademi_view, editarperfil_view


app_name = "BLSC"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('acercademi/', acercademi_view, name='acercademi'),
##### URLs PARA SIGN IN, LOGIN Y LOGOUT
    path('signin/', signin_view, name='signin'),
    path('signinok/', signinok_view, name='signinok'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name="BLSC/logout.html"), name='logout'),
##### EDITAR USUARIO
    path('editarperfil/', editarperfil_view, name='editarperfil'),
]