from django.urls import path
from app_CRUD2 import views


urlpatterns = [
    path("", views.home, name="home.html"),
]
