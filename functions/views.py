from django.shortcuts import render
from django.views.generic import View
from cronometro.settings import pusher_client

# Create your views here.
class Acoes(View):
    def get(self, request):
        return render(request, 'acoes.html')

class Start(View):
    def get(self, request):
        pusher_client.trigger('my-channel-test', 'event_start', {'event_code': '1'})
        return render(request, 'acoes.html')


class Pause(View):
    def get(self, request):
        pusher_client.trigger('my-channel-test', 'event_pause', {'event_code': '2'})
        return render(request, 'acoes.html')


class Reset(View):
    def get(self, request):
        pusher_client.trigger('my-channel-test', 'event_reset', {'evento_code': '3'})
        return render(request, 'acoes.html')


class AcrescentarUmMin(View):
    def get(self, request):
        pusher_client.trigger('my-channel-test', 'event_acresc_um', {'evento_code': '4'})
        return render(request, 'acoes.html')


class AcrescentarUmTres(View):
    def get(self, request):
        pusher_client.trigger('my-channel-test', 'event_acresc_tres', {'evento_code': '5'})
        return render(request, 'acoes.html')


class AcrescentarUmCinco(View):
    def get(self, request):
        pusher_client.trigger('my-channel-test', 'event_acresc_cinco', {'evento_code': '6'})
        return render(request, 'acoes.html')