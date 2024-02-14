from django.urls import path
from bus_auth.views import logout_user, signup, login_page

app_name = "bus_auth"

urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', login_page, name="login"),
    path('logout', logout_user, name="logout_user"),
]
