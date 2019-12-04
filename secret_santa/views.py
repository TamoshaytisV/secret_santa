from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from social_core.backends.utils import load_backends

from core.models import SecretSantaEvent, Gift, WishList


def home(request):
    if request.user.is_authenticated():
        gift = Gift.objects.filter(santa=request.user).first()
        wishlist = None
        if gift:
            presentee = (gift.presentee.get_full_name() or gift.presentee.username)
            presentee = {
                'email': gift.presentee.email,
                'name': presentee,
                'avatar': gift.presentee.avatar,
            }
            try:
                wishlist = getattr(gift.presentee, 'wishlist').get()
            except WishList.DoesNotExist:
                pass
            if wishlist:
                wishlist = wishlist.description
        else:
            presentee = None
    else:
        return render(request, 'please_login.html', {'backends': load_backends(settings.AUTHENTICATION_BACKENDS)})

    return render(
        request,
        'index.html',
        {
            'raccoons': get_user_model().objects.filter(
                as_presentee__isnull=True
            ).exclude(Q(id=request.user.id) | Q(is_staff=True)).count(),
            'presentee': presentee,
            'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS),
            'wishlist': wishlist
        }
    )
