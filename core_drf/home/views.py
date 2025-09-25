from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models 
from . import serializers

@api_view(['GET'])
def home(request):
    return Response({'message':'Welcome to home'})


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def user(request):
    if request.method == 'GET':
        objects = models.User.objects.all()
        serialized_objects = serializers.UserSerializer(objects, many=True)
        return Response(serialized_objects.data)

    elif request.method == 'POST':
        data = request.data
        data_model = serializers.UserSerializer(data = data)
        if data_model.is_valid():
            data_model.save()
            return Response(data_model.data)
        else:
            return Response(data_model.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = models.User.objects.get(id = data['id'])
        data_model = serializers.UserSerializer(obj,data=data)
        if data_model.is_valid():
            data_model.save()
            return Response(data_model.data)
        else:
            return Response(data_model.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = models.User.objects.get(id = data['id'])
        data_model = serializers.UserSerializer(obj,data=data,partial=True)
        if data_model.is_valid():
            data_model.save()
            return Response(data_model.data)
        else:
            return Response(data_model.errors)

    elif request.method == 'DELETE':
        data=request.data
        try:
            obj=models.User.objects.get(id=data['id'])
        
            obj.delete()
            return Response({"message":f"user with id:{data['id']} deleted successfully."})
        except Exception as e:
            return Response({"message":str(e)})
