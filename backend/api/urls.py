# Where all of the Django project's API are kept.

from django.urls import path

from . import views
# or written as an Explicit Import: from .view import api_home 

urlpatterns = [
    path('', views.api_home) # localhost:8000/api/
]
