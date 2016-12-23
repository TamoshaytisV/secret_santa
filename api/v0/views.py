from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.conf import settings
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import GiftSerializer
from core.models import Gift


class AssignView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        gift = Gift.objects.filter(santa=request.user).first()
        serializer = GiftSerializer(gift)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_model = get_user_model()
        if Gift.objects.filter(santa=request.user).exists():
            gift = Gift.objects.filter(santa=request.user).first()
            serializer = GiftSerializer(gift)
            return Response(serializer.data)

        created = False
        while not created:
            try:
                presentee = user_model.objects.filter(
                    ~Q(id=request.user.id),
                    as_presentee__isnull=True
                ).first()
                with transaction.atomic():
                    gift = Gift(
                        santa=request.user,
                        presentee=user_model.objects.filter(
                            as_presentee__isnull=True
                        ).first()
                    )
                    gift.save()
                created = True
            except IntegrityError:
                pass

        serializer = GiftSerializer(gift)
        return Response(serializer.data)
