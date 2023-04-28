from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    description = models.TextField()
    service = models.TextField()
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title