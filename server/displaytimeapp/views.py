from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%H:%M %p", gmtime()),
        "date": strftime("%Y-%m-%d", gmtime())
    }
    return render(request, 'index.html', context)



