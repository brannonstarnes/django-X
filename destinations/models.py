from django.db import models
from django.db.models.base import Model 
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse


class Destination(models.Model):
    location = models.CharField(max_length=60)
    description = models.TextField(max_length=256)
    traveler = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('destination_detail', args=[str(self.id)])