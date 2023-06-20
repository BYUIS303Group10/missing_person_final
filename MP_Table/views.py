from django.shortcuts import render
from .models import People
# Create your views here.


def indexPageView(request):

    return render(request, 'MP_Table/index.html',)  

def postPageView(request) :
    return render(request, 'MP_Table/post.html')

def aboutPageView(request):

    data = People.objects.all()

    context = {
        'people' : data
    }
    return render(request, 'MP_Table/about.html', context)

def personView(request):

    data = People.objects.all()

    context = {
        'people' : data
    }
    return render(request, 'MP_Table/person.html', context)
