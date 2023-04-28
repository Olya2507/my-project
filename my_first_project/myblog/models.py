from django.db import models

# Create your models here.
class Myblog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='img/')


    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Myblog', on_delete=models.CASCADE)

