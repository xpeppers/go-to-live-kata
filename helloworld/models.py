from django.db import models


class Visitors(models.Model):
    total_visitors = models.IntegerField()