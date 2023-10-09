from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_name),  # empty path represents root of this app
]
