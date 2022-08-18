from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from imdb_game_api.models import Game

class GameView(ViewSet):
    """IMDB Game game view"""

    def retrieve(self, request, pk):
        """Handle GET request for single game

        Returns:
            Response -- JSON serialized game
        """

        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """

        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """

    class Meta:
        model = Game
        fields = ('id',
                'actor_id',
                'category',
                'player',
                'correct_answers',
                'incorrect_answers',
                'score',
                'datetime',
                'outcome')
