from django.db import models

# Create your models here.

class CodeInse(models.Model):
  VI= models.CharField(max_length=50)
  code= models.IntegerField()



class Message(models.Model):
  email= models.CharField(max_length=50)
  message= models.CharField(max_length=1000)