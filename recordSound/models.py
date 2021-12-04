from django.db import models
from datetime import datetime


# Create your models here.


class RecordSound(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    recordDate = models.DateTimeField(default=datetime.now, blank=True)
    soundUrl = models.CharField(max_length=200)
    imgUrl1 = models.CharField(max_length=200, null=True)
    imgUrl2 = models.CharField(max_length=200, null=True)
    imgUrl3 = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Mqtt(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
