from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Photocard(models.Model):
    member = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return f"{self.member} - {self.album}"

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photocard = models.ForeignKey(Photocard, on_delete=models.CASCADE)
