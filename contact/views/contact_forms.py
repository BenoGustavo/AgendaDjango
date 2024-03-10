from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse("contact:create")

    # This will be the view for the contact creation form, if the user is only entering the page it won't trigger.
    if request.method == "POST":
        form = ContactForm(request.POST)

        # This is the context with all the contacts data will be passed to the template.
        context = {
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            print("valid form")
            contact = form.save(commit=False)
            contact.save()
            return redirect("contact:update", contact_id=contact.id)

        return render(
            request,
            "contact/create.html",
            context,
        )

    # This is the context with all the contacts data will be passed to the template.
    context = {
        "form": ContactForm(),
        "form_action": form_action,
    }

    return render(
        request,
        "contact/create.html",
        context,
    )


def update(request, contact_id: int):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse("contact:update", args=((contact_id,)))

    # This will be the view for the contact creation form, if the user is only entering the page it won't trigger.
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        # This is the context with all the contacts data will be passed to the template.
        context = {
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            print("valid form")
            contact = form.save(commit=False)
            contact.save()
            return redirect("contact:update", contact_id=contact.id)

        return render(
            request,
            "contact/create.html",
            context,
        )

    # This is the context with all the contacts data will be passed to the template.
    context = {
        "form": ContactForm(instance=contact),
        "form_action": form_action,
    }

    return render(
        request,
        "contact/create.html",
        context,
    )
