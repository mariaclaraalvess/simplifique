from django.contrib import admin
from django.urls import path, include  # Não se esqueça de importar o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),  # Inclui as URLs da aplicação events
]
