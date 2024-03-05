from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

from contact.views.utils import paginatorWrap


def create(request):
    # This is the context with all the contacts data will be passed to the template.
    context = {}

    return render(
        request,
        "contact/create.html",
        context,
    )
