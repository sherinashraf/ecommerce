from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'common_templates/index.html')

def common_admin(request):
    return render(request,'common_templates/admin.html')

def common_seller(request):
    return render(request,'common_templates/seller.html')

def common_customer(request):
    return render(request,'common_templates/customer.html')