from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from contact.forms import CategoryForm
from contact.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="contact:login_user")
def create_category(request):
    form_action = reverse("contact:create_category")

    context = {
        "form": CategoryForm(),
        "form_action": form_action,
        "page__tittle": "Category - Create",
        "website_tittle": "Create category -",
    }

    if request.method == "POST":
        form = CategoryForm(request.POST)

        context = {
            "form": form,
            "form_action": form_action,
            "page__tittle": "Category - Create",
        }

        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.show = True
            category.save()

            messages.success(request, "Category successfully updated")
            return redirect("contact:index")

    return render(
        request,
        "contact/register.html",
        context,
    )


@login_required(login_url="contact:login_user")
def update_category(request, category_id: int):
    category = get_object_or_404(
        Category, pk=category_id, show=True, owner=request.user
    )
    form_action = reverse("contact:update_category", args=((category_id,)))

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        context = {
            "form": form,
            "form_action": form_action,
            "page__tittle": "Category - Update",
            "what_the_page_does": "Update",
            "website_tittle": "Update category -",
        }

        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, "Category successfully updated")
            return redirect("contact:update_category", category_id=category.id)

        return render(
            request,
            "contact/create.html",
            context,
        )

    context = {
        "form": CategoryForm(instance=category),
        "form_action": form_action,
        "what_the_page_does": "Update",
        "page__tittle": "Category - Update",
        "website_tittle": "Update category -",
    }

    return render(request, "contact/register.html", context)


@login_required(login_url="contact:login_user")
def delete_category(request, category_id: int):
    category = get_object_or_404(
        Category, pk=category_id, show=True, owner=request.user
    )
    category.show = False
    category.save()
    messages.success(request, "Category successfully deleted")

    return redirect("contact:index_category")
