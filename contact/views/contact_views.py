from django.shortcuts import render
from contact.models import Contact


def index(request):
    # This will get all the contacts from the database.
    contacts = Contact.objects.filter(show=True).order_by("-id")

    table_headers = ["ID", "First name", "Last name", "Phone", "Email"]

    # This is the context with all the contacts data will be passed to the template.
    context = {
        "contacts": contacts,
        "table_headers": table_headers,
    }

    return render(
        request,
        "contact/index.html",
        context,
    )
