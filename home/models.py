from django.db import models

# Create your models here.


class Contact(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    title = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    message = models.TextField()


class LoremIpsum(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    img = models.URLField()