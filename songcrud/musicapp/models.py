from django.db import models
from datetime import datetime

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    date_of_release = models.DateField(default=datetime.today)
    likes = models.CharField(max_length=500)
    

class Lyric(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    song_id = models.CharField(max_length=40)
     
    
    
    
    