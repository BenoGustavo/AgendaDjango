from django.core.paginator import Paginator


def paginatorWrap(request, contact_list, contacts_per_page=25):

    paginator = Paginator(contact_list, contacts_per_page)
    page_number = request.GET.get("page")
    contacts_on_the_page = paginator.get_page(page_number)

    return contacts_on_the_page
