from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreate
from .models import QUiz,Student

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=QUiz
        fields=('__all__')


class UserCreateSerializer(BaseUserCreate):
    class Meta(BaseUserCreate.Meta):
        fields=[
            'id','username','email','password','first_name','last_name'
        ]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('__all__')
