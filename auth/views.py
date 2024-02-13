from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import redirect, render

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


def signup_page(request: HttpRequest):
    '''Let User sign up'''
    #redirect if user is already logged in
    if user_exist(request.user):
        return redirect("/")
    return render(request, template_name='signup.html')



def login_page(request: HttpRequest):
    '''Let User login'''
    #redirect if user is already logged in
    if user_exist(request.user):
        return redirect("/")
    return render(request, template_name="login.html")


def add_user(request: HttpRequest):
    if request.method != "POST":
        HttpResponseBadRequest('Bad Request.')

    try:
        user = Users.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'], 
            email=request.POST["email"]
        )
        login(request, user)
        return JsonResponse({
            'access':'ok'
        })
        
        
    except ValidationError as err:
        print(err.messages)
        return JsonResponse({
            "message": err.messages
        }, status=400)


def handle_login(request: HttpRequest):
    if request.method != "POST": return HttpResponseBadRequest()
    user = authenticate(username = request.POST["username"], password = request.POST["password"])
    print(user)
    if user:
        login(request,user)
        return redirect("/")
    return JsonResponse({
        "message": "not ok"
    }, status=401)


@login_required(redirect_field_name="/")
def logout_user(request):
    try:
        logout(request)
    except Exception as err:
        print(err)
        return HttpResponse("something unexpected happen")
    return redirect("/")
