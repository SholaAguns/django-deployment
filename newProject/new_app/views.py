from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord


def base(request):
    # return HttpResponse("Hello World")
    # products = Product.objects.all()
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    my_dict = {'insert_content': "Hello I am in views.py"}
    # return render(request, 'base.html', my_dict)
    return render(request, 'base.html', {'webpages_list': webpages_list})




