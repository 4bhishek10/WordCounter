import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class data(models.Model):
    email = models.CharField(max_length=50)
    text = models.CharField(max_length=1000000)
    words = models.CharField(max_length=50, default='No Value')
    sentences = models.CharField(max_length=50, default='No Value')
    characters = models.CharField(max_length=50, default='No Value')
    paragraphs = models.CharField(max_length=50, default='No Value')

    def __str__(self):
        return self.email