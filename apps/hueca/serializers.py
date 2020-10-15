from rest_framework import serializers
from .models import Hueca,Menu,Image


class HuecaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hueca
		fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'
