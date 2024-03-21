from django.shortcuts import redirect, render
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()

    # every kind of message in django
    # messages.info(request, "This is a info message")
    # messages.success(request, "This is a success message")
    # messages.warning(request, "This is a warning message")
    # messages.error(request, "This is a error message")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User successfully created")
            return redirect("contact:index")

    return render(
        request,
        "contact/register.html",
        {"form": form, "page__tittle": "Register user"},
    )


def login_user_view(request):

    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Successfully login")
            return redirect("contact:index")
        messages.error(request, "Invalid login")

    return render(request, "contact/login.html", {"form": form})


@login_required(login_url="contact:login_user")
def logout_user_view(request):
    auth.logout(request)
    return redirect("contact:login_user")


@login_required(login_url="contact:login_user")
def update_user_view(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != "POST":
        return render(request, "contact/register.html", {"form": form})

    form = RegisterUpdateForm(request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            "contact/register.html",
            {"form": form, "website_tittle": "Update user - "},
        )

    form.save()
    messages.success(request, "User successfully updated")
    return redirect("contact:update_user")
