from django.db import models



class User(models.Model):
    sentence = models.CharField(max_length=100)
    emotions = models.TextField(max_length=200)


    def __str__(self):
        return self.prefered_name
