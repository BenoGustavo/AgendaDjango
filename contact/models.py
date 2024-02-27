from django.db import models

# This module will be used to store the date and time when a contact is created.
from django.utils import timezone

# Create your models here.
"""
My model is a representation of the data that I want to store in my database.

I will create a model for a contact, which will have the following fields:
id (primary key - automatically created by Django),
first_name(String), 
last_name(String), 
phone (String), 
email (Email), 
created_at (Date), 
description (Text),


category (Foreign Key), 
show (Boolean), 
picture (image),

owner (Foreign Key), 
"""


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d/")


def __str__(self):
    return f"{self.name + self.last_name}"
