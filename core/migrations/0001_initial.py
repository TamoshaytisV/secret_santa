# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-11 16:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='as_presentee', to=settings.AUTH_USER_MODEL)),
                ('santa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='as_santa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecretSantaEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', help_text='Stuff user wants to receive as a gift.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
