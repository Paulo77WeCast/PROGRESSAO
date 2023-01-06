from django.urls import path
from .views import IndexView

urlpatterns = [
    #path('endereço/', MinhaView.as.view(), name='nome-da-url),
    path('inicio/', IndexView.as_view(), name='inicio'),
    
]
