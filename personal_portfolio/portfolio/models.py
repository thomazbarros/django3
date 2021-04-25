from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.FileField(upload_to='recordings/files/')
    url = models.URLField(blank=True)
    