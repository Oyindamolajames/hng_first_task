from dataclasses import fields
from rest_framework import serializers

from info.models import Info

class InfoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ("slackUsername", "backend", "age", "bio")