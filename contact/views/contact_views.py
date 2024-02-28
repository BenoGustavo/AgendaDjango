from django.shortcuts import render
from contact.models import Contact


def index(request):
    # This will get all the contacts from the database.
    contacts = Contact.objects.all()

    # This is the context with all the contacts data will be passed to the template.
    context = {
        "contacts": contacts,
    }

    return render(
        request,
        "contact/index.html",
        context,
    )
