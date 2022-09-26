from django.db import models

# Create your models here.


class doctor(models.Model):
    id = models.CharField(max_length=10, null=False,primary_key=True)
    username = models.CharField(max_length=10,null=False)
    password = models.CharField(null=False,max_length=10)


class client(models.Model):
    id = models.CharField(max_length=10, null=False,primary_key=True)
    name = models.CharField(max_length=10,null=False)
    mc = models.CharField(max_length=1000, default='SOME STRING')
    age = models.IntegerField(null=False)
    g = models.CharField(max_length=50, null=False)
    d = models.CharField(max_length=50, null=True)
    a = models.CharField(max_length=1000,null=True)
    q1 =  models.IntegerField(null=True)
    q2 =  models.IntegerField(null=True)
    q3 =  models.IntegerField(null=True)
    q4 =  models.IntegerField(null=True)
    q5 =  models.IntegerField(null=True)
    q6 =  models.IntegerField(null=True)
    q7 =  models.IntegerField(null=True)
    q8 =  models.IntegerField(null=True)
    q9 =  models.IntegerField(null=True)


