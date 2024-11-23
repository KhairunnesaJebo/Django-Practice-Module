from django.db import models
from musician.models import Musician

# Create your models here.

rating_choices = [('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5')]

class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(max_length=2, choices=rating_choices, default=1)
    
    def __str__(self):
        return self.name