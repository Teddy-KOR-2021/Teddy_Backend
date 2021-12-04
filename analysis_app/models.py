from django.db import models


class Sentiment(models.Model):
    date = models.CharField(max_length=30)
    anger = models.FloatField()
    disgust = models.FloatField()
    fear = models.FloatField()
    happy = models.FloatField()
    sad = models.FloatField()
    surprise = models.FloatField()
    neutral = models.FloatField()