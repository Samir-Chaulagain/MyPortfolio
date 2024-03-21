import datetime
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=15)
    url = models.URLField()
    github_link = models.URLField()
    linkedin_link = models.URLField()
    twitter_link = models.URLField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title
class Posts(models.Model):
    image = models.ImageField(upload_to='images/', default='default_image.jpg')
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)
    
    def __str__(self):
        return self.title
