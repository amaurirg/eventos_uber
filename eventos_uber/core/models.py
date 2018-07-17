from django.db import models


class EventosSP(models.Model):

	titulo = models.CharField('Título', max_length=200)
	data = models.CharField('Data', max_length=10)
	local = models.CharField('Local', max_length=50)
	endereco = models.CharField('Endereço', max_length=100)
