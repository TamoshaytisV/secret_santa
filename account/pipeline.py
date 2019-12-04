import re

from urllib import urlopen
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import redirect

from social_core.pipeline.partial import partial
from social_core.exceptions import AuthException


class InvalidRacconEmail(AuthException):
    def __str__(self):
        return 'Please use RaccoonGang corporate account.'


def check_for_raccoongang_email(
    strategy, backend, details, user=None, is_new=False, *args, **kwargs
):
    if details.get('email') and not re.search('raccoongang.com', details.get('email')):
        raise InvalidRacconEmail(backend)


@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if kwargs.get('ajax') or user and user.email:
        return
    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
            details['validation'] = True
        else:
            return redirect('account:require_email', kwargs.get('backend').name)


@partial
def mail_validation(backend, details, is_new=False, *args, **kwargs):
    requires_validation = backend.REQUIRES_EMAIL_VALIDATION or \
                          backend.setting('FORCE_EMAIL_VALIDATION', False)
    send_validation = details.get('email') and \
                      (is_new or backend.setting('PASSWORDLESS', False)) and details.get('validation')
    if requires_validation and send_validation:
        data = backend.strategy.request_data()
        if 'verification_code' in data:
            backend.strategy.session_pop('email_validation_address')
            if not backend.strategy.validate_email(details['email'],
                                           data['verification_code']):
                raise InvalidEmail(backend)
        else:
            backend.strategy.send_email_validation(backend, details['email'])
            backend.strategy.session_set('email_validation_address',
                                         details['email'])
            return backend.strategy.redirect(
                backend.strategy.setting('EMAIL_VALIDATION_URL')
            )


@partial
def disconnect(backend, user, *args, **kwargs):
    if user is None or not backend:
        return
    return
