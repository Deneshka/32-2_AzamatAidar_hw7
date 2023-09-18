from django.db import models

class Books_Library(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    cost = models.IntegerField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title