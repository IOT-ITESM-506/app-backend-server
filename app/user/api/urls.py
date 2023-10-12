"""User API routing endpoints"""

from django.urls import include, path
from rest_framework import routers

from user.api import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path("me/", views.ManageUserView.as_view(), name = "me")
]