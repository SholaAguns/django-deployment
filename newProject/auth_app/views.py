from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'auth_index.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_app:user_login'))


@login_required()
def loggedinuser(request):
    return render(request, 'loggedin_page.html')


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration.html', {'user_form': user_form,
                                                 'profile_form': profile_form,
                                                 'registered': registered

                                                 })


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('auth_app:loggedinuser'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print(f'Username: {username} and password {password}')
            return HttpResponse("Invalid login details")
    else:
        return render(request,'user_login.html')


