from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models


# New user form
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )

        # widgets = {"first_name": forms.PasswordInput()}

    def clean(self):
        # get all the data
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            error = ValidationError(
                "Your first name can't be equals to your last name",
                code="invalid_name",
            )
            self.add_error("first_name", error)
            self.add_error("last_name", error)

        return super().clean()

    # This is a custom validation for the first name field and needs to return the value of the field.
    # def clean_first_name(self):
    #     first_name = self.cleaned_data["first_name"]
    #     if first_name == "test":
    #         error = ValidationError(
    #             "don't type test as your first name, please.",
    #             code="invalid_name",
    #         )
    #         self.add_error("first_name", error)

    #     return first_name


# User registrarion form
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, min_length=3)
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField(required=True, min_length=3, max_length=100)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(
                "email",
                ValidationError("This email is already in use", code="invalid_email"),
            )
        return email
