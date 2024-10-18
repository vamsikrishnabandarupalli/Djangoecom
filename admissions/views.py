from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(req):
    return HttpResponse("Every one is attended to the class.")

def index(request):
    return render(request, 'index.html')
