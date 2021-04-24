from .import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login", obtain_auth_token),
    path("signup", views.api_signup),
    path("", views.index),
    path("show/<int:id>",views.show),
    path("create", views.create),
    path("edit/<int:id>",views.edit),
    path("delete/<int:id>",views.delete),  
]