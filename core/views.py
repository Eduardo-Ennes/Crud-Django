from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView 
from .models import Location
from .serializer import Crud_Location_Serializer

 
def home(request):
    queryset = Location.objects.all().order_by('-pk')
    context = {'datas': queryset} 
    return render(request, 'home.html', context)

def create(request):
    data = {'country': request.POST.get('country'), 'city': request.POST.get('city')}
    serializer = Crud_Location_Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return redirect('home')
    
def detail(request, id):
    ...
    
def exclude(request, id):
    data = get_object_or_404(Location, id=id)
    data.delete()
    return redirect('home')

def update(request):
    ...
