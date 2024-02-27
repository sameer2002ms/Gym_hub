from django.urls import path
from account.views import *

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", User_dashbaord, name="dashboard"),
    path("edit-profile/", edit_profile, name="edit-profile"),
]
