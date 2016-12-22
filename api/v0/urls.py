""" API v0 URLs. """
from django.conf.urls import url

from .views import AssignView


urlpatterns = [
    url(r'^assign/*$', AssignView.as_view(), name='assign'),
]
