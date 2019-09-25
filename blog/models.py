from django.db import models

# Create your models here.
class BlogConfig(models.Model):
    title = models.CharField()
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')