from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from social.backends.utils import load_backends

from core.models import SecretSantaEvent, Gift


def home(request):
    if request.user.is_authenticated():
        gift = Gift.objects.filter(santa=request.user).first()
        presentee = (gift.presentee.get_full_name() or gift.presentee.username) if gift else None
    else:
        return render(request, 'please_login.html', {'backends': load_backends(settings.AUTHENTICATION_BACKENDS)})

    return render(
        request,
        'index.html',
        {
            'raccoons': get_user_model().objects.filter(as_santa__isnull=True)
                .exclude(Q(email=request.user.email) | Q(is_staff=True))
                .count(),
            'presentee': presentee,
            'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
        }
    )
