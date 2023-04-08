from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#import json response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password

from .serializers import RAMSerializer
from .models import RAM
# Create your views here.

class HelloView(APIView):
  
    def get(self,request):
        routes = [
        "GET /api -> To get all routes of api" ,
        "GET /api/ram -> To get all details of ram utilization",

        ]
        return Response(routes)
    
class RAMView(APIView):
    def get(self,request):
        ram = RAM.objects.all()
        serializer = RAMSerializer(ram,many=True)
        return Response(serializer.data)
