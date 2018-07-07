from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from eventos_uber.core.utils import send_message, send_arquive


def home(request):
    return render(request, "index.html")


@csrf_exempt
def eventos(requests):
    json_list = json.loads(requests.body)
    # print(json_list)
    first_name = json_list['message']['chat']['first_name']
    chat_id = json_list['message']['chat']['id']
    text_message = json_list['message']['text']
    if text_message == 'eventos' or text_message == 'Eventos':
        send_message(chat_id, 'Carregando eventos ...')
        send_arquive(chat_id)
    else:
        send_message(chat_id, 'Digite eventos para obter a lista de eventos em SP')
    # print(chat_id)
    # send_message('{}, sua mensagem ao contrário é\n{}'.format(first_name, text_message[::-1]), chat_id)
    # return JsonResponse({'status': 'true', 'message': 'worked'})
    return HttpResponse()