from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns=[
#     path('login/',LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
#     path('logout/',LogoutView.as_view(next_page=''),name='logout'),
#     path('profile/',views.profile, name='profile'),
#     path('profile/edit/',views.profile_edit, name='profile_edit'),
#     path('signup/',views.signup, name='signup'),
]