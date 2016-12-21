from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class SecretSanta(models.Model):
    valid_from = models.DateTimeField(auto_now_add=timezone.now())
    valid_to = models.DateTimeField()

    def is_active(self):
        now = timezone.now().date()
        return self.valid_from <= now <= self.valid_to


class Gift(models.Model):
    santa = models.CharField(max_length=50)
    presentee = models.ForeignKey('Presentee')


class Presentee(models.Model):
    name = models.CharField(max_length=50)
