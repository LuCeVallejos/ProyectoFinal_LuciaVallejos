from django.contrib import admin
from django.urls import path
from BLSC.views import home_view
from .views import signin_view, login_view, blogpages_view, PoesiaLista, lista_poesias_view, acercademi_view

app_name = "BLSC"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('acercademi/', acercademi_view, name='acercademi'),
##### URLs PARA SIGN IN, LOGIN Y LOGOUT
    path('signin/', signin_view, name='signin'),
    path('login/', login_view, name='login'),
##### LISTA DE OBRAS
    path('blogpages/', blogpages_view, name='blogpages'),
    path('blogpagespoesias/', PoesiaLista.as_view, name='blogpagespoesias'),
    path('listapoesias/', lista_poesias_view, name='listapoesias'),
    #path('blogpagesficcion/', PoesiaDetalle.as_view, name='blogpagesficcion'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)