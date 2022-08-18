from django.db import models

class LoserGif(models.Model):
    gif = models.URLField(max_length = 200)
