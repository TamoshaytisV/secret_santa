from django.shortcuts import render

from core.models import SecretSanta


def home(request):
    return render(request, 'index.html', {'secret_santas': SecretSanta.objects.all().count()})
