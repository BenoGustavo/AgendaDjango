from django.contrib import admin

from contact.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # This will display the following fields in the admin panel.
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "created_at",
    )

    # This will order the contacts by id in descending order (it's decending because of the -).
    ordering = ("-id",)

    # This will create a search bar in the admin panel.
    search_fields = ("first_name", "last_name", "email", "id")

    # This will show 10 contacts per page.
    list_per_page = 10

    # Only show all the contacts if there are less than 100.
    list_max_show_all = 100

    # This will make the first_name and last_name fields editable in the admin panel.
    list_editable = ("first_name", "last_name")

    # This will make the id and created_at fields clickable in the admin panel.
    # You can't make the first_name and last_name clickable because they are already editable.
    list_display_links = ("id", "phone")
