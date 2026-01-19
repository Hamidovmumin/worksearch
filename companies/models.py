from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company/')
    description = models.TextField()

    def __str__(self):
        return self.name
