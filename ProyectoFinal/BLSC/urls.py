from django.contrib import admin
from django.urls import path
from BLSC.views import home_view

app_name = "BLSC"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]