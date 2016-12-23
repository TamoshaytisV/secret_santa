from django.contrib import admin

from .models import SecretSantaEvent


class SecretSantaAdmin(admin.ModelAdmin):
    """
    Admin Class for SecretSantaEvent Model.
    """
    search_fields = ('valid_from',)
    readonly_fields = ('valid_from',)
    list_display = ('valid_from', 'valid_to')
    fieldsets = [
        ('SecretSantaEvent', {
            'fields': ['valid_from', 'valid_to']
        }),
    ]

admin.site.register(SecretSantaEvent, SecretSantaAdmin)
