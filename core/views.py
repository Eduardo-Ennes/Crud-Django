from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Location
from .serializer import Crud_Location_Serializer

class Crud_Location(APIView):
    
    def get(self, request):
        queryset = Location.objects.all().order_by('-pk')
        context = {'datas': queryset} 
        return render(request, 'home.html', context)
    
    def post(self, request):
        ...
        
    def put(self, request):
        ...
        
    def delete(self, request):
        ...
