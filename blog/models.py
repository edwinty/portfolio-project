from django.db import models

# Create your models here.{}
class Article(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/') 
    
    def preview(self):
        return self.body[:280]

    def pub_date_short(self):
        return self.pub_date.strftime("%m/%Y")

    def __str__(self):
        return self.title
