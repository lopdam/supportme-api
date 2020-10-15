from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Like, Rating, Comment
from .serializers import LikeSerializer, RatingSerializer, CommentSerializer
from apps.hueca.models import Hueca
from apps.hueca.serializers import HuecaSerializer


from apps.hueca.models import Hueca
from django.contrib.auth.models import User

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser




# response list of likes
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def likes(request, hueca):
    data = Like.objects.filter(hueca=hueca).all()
    serializer = LikeSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



# response  of like
@api_view(['GET','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, hueca, user):
    #data = Like.objects.get(hueca=hueca,user=user)
    data = generics.get_object_or_404(Like,hueca=hueca,user=user)
    if(request.method=='GET'):
        serializer = LikeSerializer(data, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        data.delete()
        msg={
        'msg':'Item succsesfully delete!'
            }
        return Response(msg,status=status.HTTP_200_OK)    



# response  of like
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_like(request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)



# response hueca list of likes user
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def likes_user(request, user):
    likesList = Like.objects.filter(user=user).all()
    data=[]
    huecaList = Hueca.objects.all()
    for like in likesList:
        for hueca in huecaList:
            if like.hueca_id==hueca.id:
                data.append(hueca)

    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




#RATING SOLO SE PUEDE HACER POST Y GET
# response list of scores
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def ratings(request, hueca):
    data = Rating.objects.filter(hueca=hueca).all()
    serializer = RatingSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



# response  single user score of Hueca
@api_view(['GET','PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def rating(request, hueca, user):
    data = generics.get_object_or_404(Rating,hueca=hueca, user=user)
    if(request.method=='GET'):
        serializer = RatingSerializer(data, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif(request.method=='PUT'):
        serializer = RatingSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    msg={
        'error':'Permission Denied!'
            }
    return Response(msg,status=status.HTTP_403_FORBIDDEN)



# response  of scores
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_rating(request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)



#COMMENTS
# response list of comments
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def comments(request, hueca):
    data = Comment.objects.filter(hueca=hueca).all().order_by('created_on')
    serializer = CommentSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



# response  of comments
@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment(request,pk):
    data = generics.get_object_or_404(Comment,id=pk)
    data.delete()
    msg={
        'msg':'Item succsesfully delete!'
        }
    return Response(msg,status=status.HTTP_200_OK)  



# response  of comments
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_comment(request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)

