from django.shortcuts import render
from django.conf import settings
from social.backends.utils import load_backends

from core.models import SecretSanta


def home(request):
    return render(
        request,
        'index.html',
        {
            'secret_santas': SecretSanta.objects.all().count(),
            'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
        }
    )
