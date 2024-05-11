from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class QUiz(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    topic=models.CharField(max_length=150)
    sub_topic=models.CharField(max_length=150)
    question=models.TextField()
    level=models.CharField(max_length=12)
    option_1=models.CharField(max_length=50)
    option_2=models.CharField(max_length=50)
    option_3=models.CharField(max_length=50)


class Student(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_DIAMOND='D'
    membership_choices=[(MEMBERSHIP_BRONZE,"Bronze"),(MEMBERSHIP_GOLD,"Gold"),(MEMBERSHIP_DIAMOND,"Diamond")]


    User=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone=models.CharField(max_length=13)
    membership=models.CharField(choices=membership_choices,default=MEMBERSHIP_BRONZE,max_length=12)
    
