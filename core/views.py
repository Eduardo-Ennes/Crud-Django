from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Location
from .serializer import Crud_Location_Serializer

class Crud_Location(APIView):
    
    def get(self, request):
        queryset = Location.objects.all().order_by('-pk')
        serializer = Crud_Location_Serializer(queryset, many=True)
        context = {'datas': serializer.data} 
        return render(request, 'home.html', context)
    
    def post(self, request):
        ...
        
    def put(self, request):
        ...
        
    def delete(self, request):
        ...
