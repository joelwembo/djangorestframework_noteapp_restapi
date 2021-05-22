from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    date_field = models.DateField()

    def __str__(self):
        return self.title , self.author

   
