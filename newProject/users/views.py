from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
from .forms import NewUserForm


def default(request):
    context = {'insert_content': "Hello visitor"}
    return render(request, 'default.html', context)
    #return HttpResponse("Hello World")


def users(request):
    # user_list = Users.objects.order_by('id')
    # return render(request, 'user_page.html', {'user_list': user_list})

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return default(request)
        else:
            print('ERROR Form invalid')

    return render(request, 'user_page.html', {'form': form})
