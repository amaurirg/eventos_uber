# Generated by Django 2.0.7 on 2018-07-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventosSP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data', models.CharField(max_length=10, verbose_name='Data')),
                ('local', models.CharField(max_length=50, verbose_name='Local')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
            ],
        ),
    ]
