from django.db import models

# Create your models here.
class To_do(models.Model):
    #Store action do to task 
    content = models.TextField()

class To_cook(models.Model):
    #Store action do to task 
    content = models.TextField()

class To_wish(models.Model):
    #Store action do to task 
    content = models.TextField()