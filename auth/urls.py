from django.urls import path
from auth.views import add_user, handle_login, logout_user, login_page, signup_page

app_name = "auth"

urlpatterns = [
    path('signup', signup_page, name="signup_page"),
    path('signin', login_page, name="signin_page"),
    path('add_user', add_user, name="add_user"),
    path('logout', logout_user, name="logout_user"),
    path('handle_login', handle_login, name="handle_login")
]
