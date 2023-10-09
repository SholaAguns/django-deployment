from django.urls import path
from . import views

app_name = "new_app"

urlpatterns = [
    path('', views.base, name='base'),  # empty path represents root of this app

]
