from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
 
def about(request):
    return HttpResponse("This is a about Page")
 
def services(request):
    return render(request,'login.html')

def contact(request):
    return HttpResponse("This is a contact Page")

 
