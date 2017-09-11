# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento_trabalho1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtigoCientifico', to='evento_trabalho1.ArtigoCientifico')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Autor', to='evento_trabalho1.Autor')),
            ],
        ),
    ]