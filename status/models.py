from django.db import models
from django.conf import settings

def upload_update_image(instance, filename) -> str:
    return f'updates/{instance.user}/{filename}'


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):

    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='status_users', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.content)[:50]
