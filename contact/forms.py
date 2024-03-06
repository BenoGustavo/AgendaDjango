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
        )

        # widgets = {"first_name": forms.PasswordInput()}

    def clean(self):
        cleaned_data = self.cleaned_data

        print("limpando os dados" + str(cleaned_data))

        self.add_error(
            "first_name", ValidationError("This is a test error", code="test1")
        )
        self.add_error(
            "last_name", ValidationError("This is a test error2", code="test2")
        )

        return super().clean()
