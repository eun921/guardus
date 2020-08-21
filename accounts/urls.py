from django.urls import path, include, re_path
from accounts import views
from accounts.views import GuardusRegistrationView,ProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    re_path(r'^rest-auth/',include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', GuardusRegistrationView.as_view(), name="rest_guardus_register"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="user_profile"),
    path("edit/<int:pk>", views.ProfileView.as_view(), name="edit_user_profile"),
]