from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import redirect, render

from bus_auth.forms import LoginForm, SingupForm

from .models import Users
# Create your views here.

def user_exist(user) -> bool:
    if Users.objects.filter(id = user.id).exists():
        return True
    return False

def home(request: HttpRequest):
    if user_exist(request.user):
        return HttpResponse(f"<h1>{request.user.username}</h1>")
    return HttpResponse("<h1>This is home page</h1>")


def signup(request: HttpRequest):
    '''Let User sign up'''
    #redirect if user is already logged in
    if user_exist(request.user):
        return redirect("/")

    # if request is not POST, return signup page
    if request.method == "POST":
        signup_form = SingupForm(request.POST)

        # validate form
        if signup_form.is_valid():
            username = signup_form.cleaned_data["username"]
            email = signup_form.cleaned_data["email"]
            password = signup_form.cleaned_data["password"]
            
            try:
                user = Users.objects.create_user(username, password, email)
                user.save()
                login(request, user)
                return redirect("/")
            except ValidationError as err:
                return HttpResponseBadRequest(err)
            except Exception:
                return HttpResponse("Something unexpected happen")

        else:
            return render(request, "signup.html", {
                "form": signup_form,
                "message": "Invalid Data"
            })

    return render(request, "signup.html", {
        "form": SingupForm()
    })


def login_page(request: HttpRequest):
    '''Let User login'''
    #redirect if user is already logged in
    if user_exist(request.user):
        return redirect("/")
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username= login_form.cleaned_data["username"],
                password= login_form.cleaned_data['password'], 
            )
            
            if user:
                login(request, user)
                return redirect("/")
            else:
                print("auth fail")
                return render(request, "login.html", {
                    "message": "Invalid Credentials",
                    "form": login_form
                })
        else:
            return render(request, "login.html", {
                "form": login_form,
                "message": "Invalid Credentials"
            })

    return render(request, "login.html", {
        "form" : LoginForm()
    })


@login_required(redirect_field_name="/")
def logout_user(request):
    try:
        logout(request)
    except Exception as err:
        return HttpResponse("something unexpected happen")
    return redirect("/")
