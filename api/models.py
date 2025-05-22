from django.db import models

class User(models.Model):
    sentence = models.TextField()
    polarity = models.FloatField(null=True, blank=True)
    subjectivity = models.FloatField(null=True, blank=True)
    dominant_emotion = models.CharField(max_length=50, null=True, blank=True)
    emotion_scores = models.JSONField(null=True, blank=True)  # requires Django 3.1+

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sentence[:50]  # first 50 chars
