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

from .serializers import RAMSerializer,SysSerializer,ProcessSerializer
from .models import RAM,SysInfo,Process
# Create your views here.

class HelloView(APIView):
  
    def get(self,request):
        routes = [
        "GET /api -> To get all routes of api" ,
        "GET /api/ram -> To get all details of ram utilization",

        ]
        return Response(routes)
    
class SysView(APIView):
    def get(self,request):
        sys = SysInfo.objects.all()
        serializer = SysSerializer(sys,many=True)
        return Response(serializer.data)


class RAMView(APIView):
    def get(self,request):
        ram = RAM.objects.all()
        serializer = RAMSerializer(ram,many=True)
        return Response(serializer.data)

class ProcessView(APIView):
    def get(self,request):
        process = Process.objects.all()
        serializer = ProcessSerializer(process,many=True)
        return Response(serializer.data)
