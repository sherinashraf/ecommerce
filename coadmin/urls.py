from django.urls import path
from . import views
app_name = 'coadmin'

urlpatterns=[
    path('home',views.coadmin_home,name = 'home')
]