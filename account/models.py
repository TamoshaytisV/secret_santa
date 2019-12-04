from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __unicode__(self):
        return u'{}'.format(self.username)

    def full_name(self):
        name = self.get_full_name()
        if name:
            return name
        return self.get_username()


class EmailChange(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    verification_key = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'({}) {} --> {}'.format(
            self.user.username,
            self.user.email,
            self.email
        )
