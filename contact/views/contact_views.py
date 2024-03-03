from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):
    # This will get all the contacts from the database.
    contacts = Contact.objects.filter(show=True).order_by("-id")

    table_headers = ["ID", "First name", "Last name", "Phone", "Email"]

    # This is the context with all the contacts data will be passed to the template.
    context = {
        "contacts": contacts,
        "table_headers": table_headers,
        "website_tittle": "Contacts -",
    }

    return render(
        request,
        "contact/index.html",
        context,
    )


def single_contact(request, contact_id: int):
    # This will get the contact from the database and if it doesn't exist returns a 404 error.
    contact = get_object_or_404(Contact.objects.filter(pk=contact_id), show=True)

    # This is the context with the contact data will be passed to the template.
    context = {
        "contact": contact,
        "website_tittle": contact.first_name + " " + contact.last_name + " -",
    }

    return render(
        request,
        "contact/single_contact.html",
        context,
    )
