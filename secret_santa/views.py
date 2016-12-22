from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from social.backends.utils import load_backends

from core.models import SecretSanta


def home(request):
    return render(
        request,
        'index.html',
        {
            'secret_santas': get_user_model().objects.filter(as_santa__isnull=True).count(),
            'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
        }
    )
