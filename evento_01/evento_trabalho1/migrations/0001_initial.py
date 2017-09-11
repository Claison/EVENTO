# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventoPrincipal', models.CharField(max_length=128)),
                ('nome', models.CharField(max_length=128)),
                ('data_inicio', models.DateTimeField()),
                ('logotipo', models.CharField(max_length=128)),
                ('palavrasChave', models.CharField(max_length=128)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('endereco', models.CharField(max_length=250)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento_trabalho1.Pessoa')),
                ('curriculo', models.CharField(max_length=128)),
                ('artigos', models.CharField(max_length=128, null=True)),
                ('pai', models.CharField(max_length=128, null=True)),
            ],
            bases=('evento_trabalho1.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento_trabalho1.Evento')),
                ('issn', models.CharField(max_length=9)),
            ],
            bases=('evento_trabalho1.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento_trabalho1.Pessoa')),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('evento_trabalho1.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento_trabalho1.Pessoa')),
                ('cnpj', models.CharField(max_length=11)),
                ('razaoSocial', models.CharField(max_length=100)),
            ],
            bases=('evento_trabalho1.pessoa',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realizadores', to='evento_trabalho1.PessoaFisica'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evento', to='evento_trabalho1.EventoCientifico'),
        ),
    ]
