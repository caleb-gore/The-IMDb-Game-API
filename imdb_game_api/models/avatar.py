from django.db import models

class Avatar(models.Model):
    image = models.ImageField(
        upload_to='avatarimages',
        height_field=None,
        width_field=None,
        max_length=None,
        null=True
)
