import email
from typing import Optional
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=37)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=122)
    date = models.DateField()
    
    def __str__(self):
        return self.name
