from django.db import models

# Create your models here.

class Info (models.Model):
    slackUsername = models.CharField(max_length = 225)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.slackUsername}"