from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            'snippet_set',
        )


class SnippetSerializer(serializers.ModelSerializer):
    owner = UserSerializer

    class Meta:
        model = Snippet
        fields = (
            'pk',
            'owner',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )
