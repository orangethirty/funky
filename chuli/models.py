from django.db import models


class Puli(models.Model):
    title = models.TextField()
    url = models.TextField() #space is cheap.
    description = models.TextField()
    ranking = models.IntegerField()
    points = models.IntegerField() #default is 1 point for every new Puli.
    

