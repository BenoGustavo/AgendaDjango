from django.db import models

# This module will be used to store the date and time when a contact is created.
from django.utils import timezone

from django.contrib.auth.models import User

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


class Category(models.Model):
    # This will display the name of the category in the admin panel,
    # some times the plural isn't right so you need to change it manualy.
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d/")

    # On delete set null, because the owner can be deleted
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name + ' ' + self.last_name}"
