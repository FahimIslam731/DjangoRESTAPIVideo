from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='uploaded_videos/')
    detected_emotion = models.CharField(max_length=50)

    def __str__(self):
        return f"Emotion Result for {self.video.name}"
