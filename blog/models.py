#coding=utf-8
from django.db import models

# Create your models here.

'''
用户类
Ron
2016-07-11
'''

class Users(models.Model):
    userName = models.CharField(max_length = 64)
    passWord = models.CharField(max_length = 64)
    validStatus = models.CharField(max_length = 1)