from django.urls import path
from . import views

app_name = "auth_app"

urlpatterns = [
    path('', views.index, name='auth_index'),  # empty path represents root of this app
    path('registration/', views.registration, name="registration"),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('loggedinuser/', views.loggedinuser, name='loggedinuser')
]
