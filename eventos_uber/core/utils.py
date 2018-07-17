from decouple import config
import datetime
import requests, bs4, re

from eventos_uber.core.models import EventosSP

TOKEN = config('TOKEN')
arquivo = './eventos.txt'

url_base = 'https://www.ticket360.com.br'
res = requests.get(url_base)
res.raise_for_status()
page = bs4.BeautifulSoup(res.text, "html.parser")

calendario = {'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6, 'Julho': 7,
              'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12}


def send_arquive(chat_id):
	with open(arquivo) as file_eventos:
		texto = file_eventos.read()
	data = {'chat_id': chat_id, 'text': texto}
	url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
	requests.post(url, data = data)


def send_message(chat_id, text):
	data = {'chat_id': chat_id, 'text': text}
	url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
	requests.post(url, data = data)


def evento(src):
	res_ev = requests.get(src)
	res_ev.raise_for_status()
	page = bs4.BeautifulSoup(res_ev.text, "html.parser")
	box = page.find('div', {'class': 'media-body eventos'})
	title = box.find('h4').text
	data_hora = box.find('p', {'class': 'data'}).text
	logradouro = box.find('p', {'class': 'notranslate'}).text
	loc = re.split('\n\r\n', logradouro.strip())
	endereco = (' ').join(loc[1].split())
	local = loc[0]
	a = re.split(r'-', data_hora)
	data = [i.strip() for i in a]
	# sep = data[0].split()
	# dia = int(sep[1])
	# mes = calendario[sep[-1]]
	# data_evento = datetime.datetime(2018, mes, dia, 0, 0, 0)
	# qtde_dias = data_evento - datetime.datetime.now()
	# if qtde_dias.days == 3:
	# 	return 'FIM'
	# else:
	# EventosSP.objects.create(titulo='title', data='data', local='local', endereco='endereco')
	# EventosSP.objects.create(titulo=title, data=(' - ').join(data), local=local, endereco=endereco)
	return [title, (' - ').join(data), local, endereco]


# data_atual = datetime.datetime.now()
# data_dia_seguinte = datetime.timedelta(days=1)

# with open(arquivo) as file_eventos:
# 	texto = file_eventos.read()
# 	data_atualizacao = re.search(r'[0-9]{2}/[0-9]{2}/[0-9]{4}', texto)
# if data_atualizacao.group() == data_dia_seguinte.strftime('%d/%m/%Y'):
# 	# print('Já está atualizado')
# 	pass
# else:
# 	with open(arquivo, 'w') as file_eventos:
# 		file_eventos.write('Eventos em SP\nAtualizado em {}\n\n\n'.format(data_atual.strftime('%d/%m/%Y')))
# 	boxes = page.find('ul', {'class': 'galeria destaque'}).find_all('a')
# 	for i in boxes:
# 		link = url_base + i.get('href')
# 		if evento(link) == 'FIM':
# 			break
# 		else:
# 			with open(arquivo, 'a') as file_eventos:
# 				for event in evento(link):
# 					file_eventos.write(event + '\n')
# 				file_eventos.write('\n')


def testedb(chat_id):
	# pass
	boxes = page.find('ul', {'class': 'galeria destaque'}).find_all('a')
	for i in boxes:
		link = url_base + i.get('href')
		event = evento(link)
		for i in event:
			send_message(chat_id, i)
	# 		for i in event:
	# 	# 		send_message(chat_id, i)
	# 			EventosSP.objects.create(titulo=i[0], data=i[1], local=i[2], endereco=i[3])
