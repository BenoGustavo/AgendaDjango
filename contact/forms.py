from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
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
