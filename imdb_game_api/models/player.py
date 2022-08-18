from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favMovie = models.CharField(max_length=10)
    favGenre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    avatar = models.ForeignKey("Avatar", on_delete=models.CASCADE)
