from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"login.html")

def dashboard(request):
    return render(request,"dashbord.html")