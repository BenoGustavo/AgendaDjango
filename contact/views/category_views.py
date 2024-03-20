from django.shortcuts import get_object_or_404, render
from contact.models import Category
from django.contrib.auth.decorators import login_required
from contact.views.utils import paginatorWrap


@login_required(login_url="contact:login_user")
def index_category(request):
    categories = Category.objects.filter(owner=request.user, show=True)

    # display 25 contacts per page
    categories_on_the_page = paginatorWrap(request, categories, 25)

    table_headers = ["ID", "Name", "Owner"]

    context = {
        "categories": categories_on_the_page,
        "table_headers": table_headers,
        "website_tittle": "Categories -",
    }

    return render(
        request,
        "contact/category_index.html",
        context,
    )


@login_required(login_url="contact:login_user")
def single_category(request, category_id: int):
    category = get_object_or_404(
        Category, pk=category_id, show=True, owner=request.user
    )

    context = {
        "category": category,
        "website_tittle": f"{category.name} -",
        "delete__button__text": "Delete",
        "Form__method": "GET",
    }

    return render(
        request,
        "contact/single_category.html",
        context,
    )
