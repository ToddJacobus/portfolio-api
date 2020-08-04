from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    comments = models.TextField(max_length=10000)

    def __str__(self):
        return self.name
