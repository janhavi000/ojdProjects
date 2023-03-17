from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')
    
def about_view(request):
    return render(request,'about.html')

def teacher_view(request):
    return render(request,'teacher.html')

def vehicle_view(request):
    return render(request,'vehicle.html')

def contact_view(request):
    return render(request,'contact.html')

