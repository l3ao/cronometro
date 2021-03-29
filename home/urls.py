from django.urls import path
from home.views import Home, Cronometro

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cronometro/', Cronometro.as_view(), name='cronometro')
]
