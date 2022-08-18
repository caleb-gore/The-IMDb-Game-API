from django.db import models

class WinnerGif(models.Model):
    gif = models.URLField(max_length = 200)
    