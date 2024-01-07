from django.shortcuts import render



# Create your views here.
def bloghtml(request):
    return render(request,'blog.html')

def abouthtml(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')