from django.shortcuts import render

# Create your views here.
def coadmin_home(request):
    return render(request,'coadmin_templates/home.html')