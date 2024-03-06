from django.shortcuts import render
from contact.forms import ContactForm


def create(request):
    # This will be the view for the contact creation form, if the user is only entering the page it won't trigger.
    if request.method == "POST":
        # This is the context with all the contacts data will be passed to the template.
        context = {"form": ContactForm(request.POST)}

        return render(
            request,
            "contact/create.html",
            context,
        )

    # This is the context with all the contacts data will be passed to the template.
    context = {
        "form": ContactForm(),
    }

    return render(
        request,
        "contact/create.html",
        context,
    )
