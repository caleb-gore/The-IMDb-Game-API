from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from imdb_game_api.models import Avatar

class AvatarView(ViewSet):
    """IMDB Game avatar view"""

    def retrieve(self, request, pk):
        """Handle GET request for single avatar

        Returns:
            Response -- JSON serialized avatar
        """

        avatar = Avatar.objects.get(pk=pk)
        serializer = AvatarSerializer(avatar)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all avatars

        Returns:
            Response -- JSON serialized list of game types
        """

        avatars = Avatar.objects.all()
        serializer = AvatarSerializer(avatars, many=True)
        return Response(serializer.data)

class AvatarSerializer(serializers.ModelSerializer):
    """JSON serializer for avatars
    """

    class Meta:
        model = Avatar
        fields = ('id', 'image')
