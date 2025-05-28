from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Location

class Crud_Location(APIView):
    def get(self, request):
        data = Location.objects.all()
        context = {'datas': data}
        return render(request, 'home.html', context)
    
    def post(self, request):
        ...
        
    def put(self, request):
        ...
        
    def delete(self, request):
        ...
