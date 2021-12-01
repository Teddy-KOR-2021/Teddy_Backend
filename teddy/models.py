from django.db import models


class Test(models.Model):
    test = models.CharField(max_length=200)
    photo = models.FileField()

    def __str__(self):
        return self.test
