from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QUiz,Student
from .serializers import QuizSerializer,StudentSerializer
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin


class QuizListView(APIView):
    def get(self,request):
        queryset=QUiz.objects.all()
        serializing_object=QuizSerializer(queryset,many=True)
        return Response(serializing_object.data)
    
    def post(self,request):
        serializing_data=QuizSerializer(data=request.data)
        serializing_data.is_valid(raise_exception=True)
        serializing_data.save()
        return Response(serializing_data.data)
    


class SingleQuizView(APIView):
    def get(self,request,id):
        query=get_object_or_404(QUiz,id=id)
        serializing_object=QuizSerializer(query)
        return Response(serializing_object.data)
    def put(self,request,id):
        query=get_object_or_404(QUiz,id=id)
        serializing_object=QuizSerializer(query,data=request.data)
        serializing_object.is_valid(raise_exception=True)
        serializing_object.save()
        return Response(serializing_object.data)
    
    def delete(self,request,id):
        query=get_object_or_404(QUiz,id=id)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




class ProfileViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer