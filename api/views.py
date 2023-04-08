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

    def post(self,request):
        serializer = SysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RAMView(APIView):
    def get(self,request):
        ram = RAM.objects.all()
        serializer = RAMSerializer(ram,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = RAMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProcessView(APIView):
    def get(self,request):
        process = Process.objects.all()
        serializer = ProcessSerializer(process,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
