from django.contrib import admin

from .models import SecretSantaEvent, Gift, WishList


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


class GiftAdmin(admin.ModelAdmin):
    """
    Admin Class for Gift Model.
    """
    list_display = ('santa', 'presentee')


class WishListAdmin(admin.ModelAdmin):
    """
    Admin Class for WishList Model.
    """
    list_display = ('user', 'description')


admin.site.register(Gift, GiftAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(SecretSantaEvent, SecretSantaAdmin)
