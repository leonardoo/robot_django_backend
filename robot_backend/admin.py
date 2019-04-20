from django.contrib import admin

from . import models


@admin.register(models.UserSecretModel)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'secret_key', "public_key", "active", "user_")
    search_fields = ('user__username',)

    def user_(self, obj):
    	return obj.user.username

    def queryset(self, request, queryset):
        return queryset.select_related("user")
