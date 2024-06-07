from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    
class Cartoon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_image = models.ImageField(upload_to='posters/')
