from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from social.backends.utils import load_backends

from core.models import SecretSanta, Gift


def home(request):
    gift = Gift.objects.filter(santa=request.user).first()
    presentee = (gift.presentee.get_full_name() or gift.presentee.username) if gift else None

    return render(
        request,
        'index.html',
        {
            'secret_santas': get_user_model().objects.filter(as_santa__isnull=True).count(),
            'presentee': presentee,
            'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
        }
    )
