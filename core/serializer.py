from rest_framework import serializers
from .models import Location

class Crud_Location_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'country', 'city', 'created', 'update']
        
    def validate(self, data):
        country = data.get('country')
        city = data.get('city')
        print(country, city) # Location object

        if country is not None:
            if country == '' or country == ' ':
                raise serializers.ValidationError('O campos país não pode ser vazio.')
            
            if len(country) > 100:
                raise serializers.ValidationError('O campo país deve conter no máximo 100 caracteres.')
            
        if city is not None:
            if city == '' or city == ' ':
                raise serializers.ValidationError('O campos cidade não pode ser vazio.')
            if len(city) > 100:
                raise serializers.ValidationError('O campo cidade deve conter no máximo 100 caracteres.')
            
        if country is not None and city is not None:
            if Location.objects.filter(country=country, city=city).exists():
                raise serializers.ValidationError('Este destino já foi cadastrado.')
            
        return data
        