from django.urls import path
from functions.views import Acoes, Start, Pause, Reset, AcrescentarUmMin, AcrescentarUmTres, AcrescentarUmCinco

urlpatterns = [
    path('', Acoes.as_view(), name='acoes'),
    path('start/', Start.as_view(), name='start'),
    path('pause/', Pause.as_view(), name='pause'),
    path('reset/', Reset.as_view(), name='reset'),
    path('acrescentar-um-min/', AcrescentarUmMin.as_view(), name='acresc-um-min'),
    path('acrescentar-um-tres/', AcrescentarUmTres.as_view(), name='acresc-um-tres'),
    path('acrescentar-um-cinco/', AcrescentarUmCinco.as_view(), name='acresc-um-cinco'),
]
