from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView 
from .models import Location
from .serializer import Crud_Location_Serializer

 
def home(request):
    queryset = Location.objects.all().order_by('-pk')
    context = {'datas': queryset} 
    return render(request, 'home.html', context)

def create(request):
    country = request.POST.get('country')
    city = request.POST.get('city')
    if country is not None and city is not None:
        data = {'country': request.POST.get('country'), 'city': request.POST.get('city')}
        serializer = Crud_Location_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
    return redirect('home')
    
def detail(request, id):
    data = Location.objects.filter(id=id).first()
    if data:
        context = {'data': data}
        return render(request, 'details.html', context)
    return redirect('home')
    
def exclude(request, id):
    data = get_object_or_404(Location, id=id)
    data.delete()
    return redirect('home')

def update(request):
    id = request.POST.get('id')
    obj_location = get_object_or_404(Location, id=id)
    print('****************************')
    print(obj_location)
    data = {'country': request.POST.get('country'), 'city': request.POST.get('city')}
    serializer = Crud_Location_Serializer(instance=obj_location, data=data, partial=True)
    if serializer.is_valid():
        print('VÁLIDO')
        serializer.save()
    return redirect('home')

'''
venv/scripts/activate
python manage.py runserver
'''
