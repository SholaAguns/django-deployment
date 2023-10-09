from django.shortcuts import render


def index(request):
    my_dict = {'text': 'This is the text and here is a number', 'number': 100}
    return render(request, 'templates_index.html', my_dict)


def relative(request):
    return render(request, 'relative_url.html')


def other(request):
    return render(request, 'other.html')
