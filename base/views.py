from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def page1(request):
    return render(request, 'base/page1.html')

def page2(request):
    return render(request, 'base/page2.html')