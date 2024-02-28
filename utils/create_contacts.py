"""
WARNING - THIS MODULE WILL ERASE EVERYTHING IN THE CONTACTS AND CATEORIES TABLES AND WILL CREATE NEW FAKE DATA

This module is used to create FAKE contacts for the application using the faker lib.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_CONTACTS = 1000

# Add the project to sys.path
sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"

# remove the timezone warning
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker

    from contact.models import Contact, Category

    Contact.objects.all().delete()
    Category.objects.all().delete()

    faker_instance = faker.Faker("pt_BR")
    categories = ["Family", "Friends", "Work", "Others"]

    django_categories = [Category(name=category_name) for category_name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_CONTACTS):
        profile = faker_instance.profile()
        email = profile["mail"]
        first_name, last_name = profile["name"].split(" ", 1)
        phone = faker_instance.phone_number()
        created_at: datetime = faker_instance.date_this_year()
        description = faker_instance.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_at=created_at,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
