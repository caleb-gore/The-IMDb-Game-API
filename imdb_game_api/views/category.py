from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from imdb_game_api.models import Category

class CategoryView(ViewSet):
    """IMDB Game category view"""

    def retrieve(self, request, pk):
        """Handle GET request for single category

        Returns:
            Response -- JSON serialized category
        """

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """

    class Meta:
        model = Category
        fields = ('id', 'list_id', 'name')
