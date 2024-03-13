"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from contact import views

app_name = "contact"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),
    # CRUD of the contacts
    path("contact/<int:contact_id>/", views.single_contact, name="single_contact"),
    path("contact/create/", views.create, name="create"),
    path("contact/<int:contact_id>/update/", views.update, name="update"),
    path("contact/<int:contact_id>/delete/", views.delete, name="delete"),
    # CRU of the user
    path("user/create/", views.register, name="create_user"),
]
