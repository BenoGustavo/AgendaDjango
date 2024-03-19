from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from . import models


# New user form
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
                "required": False,
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


# User update form
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages={"required": "This field is required"},
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages={"required": "This field is required"},
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label="Confirm passoword",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Use the same password as before.",
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        passoword1 = self.cleaned_data.get("password1")
        passoword2 = self.cleaned_data.get("password2")

        if passoword1 and passoword2:
            if passoword1 != passoword2:
                self.add_error(
                    "password2",
                    ValidationError(
                        "The passwords doesn't match", code="invalid_password"
                    ),
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        logged_user_email = self.instance.email

        if logged_user_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    "email",
                    ValidationError(
                        "This email is already in use", code="invalid_email"
                    ),
                )
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if not password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as e:
                self.add_error("password1", ValidationError(e), code="invalid_password")

        return password1


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = (
            "name",
            "description",
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        owner = self.instance.owner

        if models.Category.objects.filter(name=name, owner=owner).exists():
            self.add_error(
                "name",
                ValidationError(
                    "This category already exists, try another one", code="invalid_name"
                ),
            )
