from django.db import models

class Game(models.Model):
    actor_id = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()
    score = models.IntegerField()
    datetime = models.DateTimeField()
    outcome = models.CharField(max_length=10)
