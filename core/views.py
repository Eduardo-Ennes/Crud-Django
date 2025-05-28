from django.shortcuts import render, redirect
from rest_framework.views import APIView 
from .models import Location
from .serializer import Crud_Location_Serializer

class Crud_Location(APIView):
    
    def get(self, request):
        queryset = Location.objects.all().order_by('-pk')
        context = {'datas': queryset} 
        return render(request, 'home.html', context)
    
    def post(self, request):
        serializer = Crud_Location_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('home')
        
    def put(self, request):
        ...
        
    def delete(self, request):
        ...
