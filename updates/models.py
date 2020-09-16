from django.db import models
from django.conf import settings

def upload_update_image(instance, filename) -> str:
    return f'updates/{instance.user}/{filename}'

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content
