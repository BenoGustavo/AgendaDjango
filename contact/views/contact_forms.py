from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url="contact:login_user")
def create(request):
    form_action = reverse("contact:create")

    # This will be the view for the contact creation form, if the user is only entering the page it won't trigger.
    if request.method == "POST":
        # I"m sending the user to check the categories that belongs to the him on the ContactForm model
        form = ContactForm(request.POST, request.FILES, user=request.user)

        # This is the context with all the contacts data will be passed to the template.
        context = {
            "form": form,
            "form_action": form_action,
            "what_the_page_does": "Create",
            "website_tittle": "Create contact -",
        }

        if form.is_valid():
            print("valid form")
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect("contact:update", contact_id=contact.id)

        return render(
            request,
            "contact/create.html",
            context,
        )

    # This is the context with all the contacts data will be passed to the template.
    context = {
        # I"m sending the user to check the categories that belongs to the him on the ContactForm model
        "form": ContactForm(user=request.user),
        "form_action": form_action,
        "what_the_page_does": "Create",
        "website_tittle": "Create contact -",
    }

    return render(
        request,
        "contact/create.html",
        context,
    )


@login_required(login_url="contact:login_user")
def update(request, contact_id: int):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse("contact:update", args=((contact_id,)))

    # This will be the view for the contact creation form, if the user is only entering the page it won't trigger.
    if request.method == "POST":
        # I"m sending the user to check the categories that belongs to the him on the ContactForm model
        form = ContactForm(
            request.POST, request.FILES, instance=contact, user=request.user
        )

        # This is the context with all the contacts data will be passed to the template.
        context = {
            "form": form,
            "form_action": form_action,
            "what_the_page_does": "Update",
            "website_tittle": "Update contact -",
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
        # I"m sending the user to check the categories that belongs to the him on the ContactForm model
        "form": ContactForm(instance=contact, user=request.user),
        "form_action": form_action,
        "what_the_page_does": "Update",
        "website_tittle": "Update contact -",
    }

    return render(
        request,
        "contact/create.html",
        context,
    )


@login_required(login_url="contact:login_user")
def delete(request, contact_id: int):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)

    if request.method == "POST":
        contact.delete()
        return redirect("contact:index")

    return render(
        request,
        "contact/single_contact.html",
        {
            "contact": contact,
            "delete__button__text": "Are you sure you want to delete this contact?",
            "website_tittle": "Manage contact -",
            "form__method": "POST",
            "website_tittle": "Delete contact -",
        },
    )
