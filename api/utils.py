from random import randint
from django.db.models.aggregates import Count
from django.contrib.auth import get_user_model
from django.db.models import Q


def get_random_presentee(user_id):
    """
    Return random Presentee.
    """
    user_model = get_user_model()
    qs = user_model.objects.filter(
        ~Q(id=user_id),
        as_presentee__isnull=True
    )
    count = qs.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    return qs[random_index]
