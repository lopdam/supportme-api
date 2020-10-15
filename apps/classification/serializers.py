from rest_framework import serializers
from .models import City,Category

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'
