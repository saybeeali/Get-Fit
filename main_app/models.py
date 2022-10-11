from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bodypart(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    Benefits = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

        

class Exercise(models.Model):


    name = models.CharField(max_length=100)
    Instructions = models.TextField(max_length=500)
    bodypart = models.ForeignKey(Bodypart, on_delete=models.CASCADE, related_name='exercise')

    def __str__(self):
        return self.name


    



    
