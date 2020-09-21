from django.forms import fields
from rest_framework import serializers

from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'user',
            'content',
            'image',
        )

    # def validate_content(sef, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is too long")
    #     return value

    def validate(self, data):
        content = data.get('content', None)

        if content == "":
            content = None
        
        image = data.get('image', None)

        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required')
        return data
