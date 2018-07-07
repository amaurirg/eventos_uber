from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from eventos_uber.core.utils import send_message


def home(request):
    return render(request, "index.html")


@csrf_exempt
def eventos(requests):
    json_list = json.loads(requests.body)
    # print(json_list)
    first_name = json_list['message']['chat']['first_name']
    chat_id = json_list['message']['chat']['id']
    text_message = json_list['message']['text']
    print(chat_id)
    send_message('{}, sua mensagem ao contrário é\n{}'.format(first_name, text_message[::-1]), chat_id)
    # return JsonResponse({'status': 'true', 'message': 'worked'})
    return HttpResponse()