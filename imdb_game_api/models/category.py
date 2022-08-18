from django.db import models

class Category(models.Model):
    list_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
