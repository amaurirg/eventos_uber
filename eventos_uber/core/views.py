from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from eventos_uber.core.utils import send_message, send_arquive, testedb


def home(request):
    return render(request, "index.html")


@csrf_exempt
def eventos(requests):
    json_list = json.loads(requests.body)
    chat_id = json_list['message']['chat']['id']
    text_message = json_list['message']['text']
    if text_message == 'eventos' or text_message == 'Eventos':
        send_message(chat_id, 'Carregando eventos ...')
        # send_arquive(chat_id)
        # testedb(chat_id)
        pass
    else:
        send_message(chat_id, 'Digite eventos para obter a lista de eventos em SP')
    return HttpResponse()