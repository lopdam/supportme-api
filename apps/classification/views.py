from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import City, Category
from .serializers import CitySerializer, CategorySerializer

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# response list of cities
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def cities(request):
    data = City.objects.all().order_by('name')
    serializer = CitySerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



# response list of categories
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def categories(request):
    data = Category.objects.all().order_by('name')
    serializer = CategorySerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



# response a single city
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def city(request, pk):
    #data = City.objects.get(id=pk)
    data=generics.get_object_or_404(City,id=pk)
    serializer = CitySerializer(data, many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)



# response a single category
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def category(request, pk):
    #data = Category.objects.get(id=pk)
    data=generics.get_object_or_404(Category,id=pk)
    serializer = CategorySerializer(data, many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)
