from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics

from .models import Hueca, Menu, Image
from .serializers import HuecaSerializer, MenuSerializer, ImageSerializer

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

#Calculate Distance
from .distance_location import is_near

#from rest_framework.views import APIView
#from rest_framework.viewsets import ViewSet, ModelViewSet



#IMAGES
# response  a single Image
@api_view(['GET','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def image(request, pk):
    
    #data = Image.objects.get(hueca=hueca)
    if(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Image,id=pk)
        data.delete()
        msg={
        'msg':'Item succsesfully delete!'
            }
        return Response(msg,status=status.HTTP_200_OK) 

    elif(request.method=='GET'):
        data = generics.get_object_or_404(Image,id=pk)
        serializer = ImageSerializer(data, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    msg={
        'error':'Permission Denied!'
            }
    return Response(msg,status=status.HTTP_403_FORBIDDEN)



# response  of  image
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_image(request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)  



# response list of images
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def images(request,hueca):
    data = Image.objects.filter(hueca=hueca).all()
    serializer = ImageSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




#MENU
# response  a single menu
@api_view(['GET','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def menu(request, pk):
    data = generics.get_object_or_404(Menu,id=pk)
    #data = Image.objects.get(hueca=hueca)
    if(request.method=='GET'):
        serializer = MenuSerializer(data, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif(request.method=='DELETE' and request.user.is_authenticated):
        data.delete()
        msg={
        'msg':'Item succsesfully delete!'
            }
        return Response(msg,status=status.HTTP_200_OK)
    msg={
        'error':'Permission Denied!'
            }
    return Response(msg,status=status.HTTP_403_FORBIDDEN)



# response  of  menu
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_menu(request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)  



# response list of menu
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def menus(request,hueca):
    data = Menu.objects.filter(hueca=hueca).all()
    serializer = MenuSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




#HUECA
# response list of huecas
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def huecas(request):
    data = Hueca.objects.all()
    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




# response  a single hueca
@api_view(['GET','DELETE','PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def hueca(request, pk):
    data = generics.get_object_or_404(Hueca,id=pk)
    #data = Hueca.objects.get(id=pk)
    if(request.method=='GET'):
        serializer = HuecaSerializer(data, many=False)
        return Response(serializer.data)
    elif(request.method=='DELETE' and request.user.is_authenticated):
        data.delete()
        msg={
        'msg':'Item succsesfully delete!'
            }
        return Response(msg,status=status.HTTP_200_OK)  
    elif(request.method=='PUT' and request.user.is_authenticated):
        serializer = HuecaSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    msg={
        'error':'Permission Denied!'
            }
    return Response(msg,status=status.HTTP_403_FORBIDDEN)




# response  of  huecas
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_hueca(request):
        serializer = HuecaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  



#FILTROS HUECAS
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def huecas_city(request,city):
    data = Hueca.objects.filter(city=city).all()
    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def huecas_category(request,category):
    data = Hueca.objects.filter(category=category).all()
    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def huecas_search(request,search):
    data = Hueca.objects.filter(name__startswith=search).all()
    #data = Hueca.objects.filter(name=search).all()
    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




# response list of huecas
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def huecas_location(request,latitude,longitude,km):
    #current User Location
    try:
        latitude=float(latitude)
        longitude=float(longitude)
        km = float(km)
    except ValueError:
        msg={
        'msg':'No data avalible.!'
            }
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    #print("latitude: "+str(latitude))
    #print("longitude: "+str(longitude))
    #print("km: "+str(km))

    data = Hueca.objects.all()
    #print(data)
    listHuecas=[]
    for hueca in data:
        if(is_near(latitude, longitude, hueca.latitude, hueca.longitude, km)):
            serializer = HuecaSerializer(hueca, many=False)
            listHuecas.append(serializer.data)

    return Response(listHuecas, status=status.HTTP_200_OK)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def huecas_user(request,user):
    data = Hueca.objects.filter(user=user).all()
    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)