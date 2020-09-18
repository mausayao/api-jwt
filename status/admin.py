from django.contrib import admin
from .models import Status


@admin.register(Status)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('user', 'content',)
