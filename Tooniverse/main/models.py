from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    
class Cartoon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_image = models.ImageField(upload_to='posters/')


class Message(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author + ": " + self.content[:50]