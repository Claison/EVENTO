# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento_trabalho1', '0003_auto_20170911_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorArtigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtigoCientifico', to='evento_trabalho1.ArtigoCientifico')),
            ],
        ),
        migrations.RemoveField(
            model_name='autor',
            name='pai',
        ),
        migrations.AlterField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realizadores', to='evento_trabalho1.Pessoa'),
        ),
        migrations.AddField(
            model_name='autorartigo',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Autor', to='evento_trabalho1.Autor'),
        ),
    ]
