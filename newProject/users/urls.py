from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),  # empty path represents root of this app
    path('default', views.default)
]