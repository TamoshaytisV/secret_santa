from django.contrib import admin

from .models import SecretSanta


class SecretSantaAdmin(admin.ModelAdmin):
    """
    Admin Class for SecretSanta Model.
    """
    search_fields = ('valid_from',)
    readonly_fields = ('valid_from',)
    list_display = ('valid_from', 'valid_to')
    fieldsets = [
        ('SecretSanta', {
            'fields': ['valid_from', 'valid_to']
        }),
    ]

admin.site.register(SecretSanta, SecretSantaAdmin)
