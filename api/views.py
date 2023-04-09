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

from .serializers import RAMSerializer,SysSerializer,ProcessSerializer,CustomUserSerializer, TPInfoSerializer
from .models import RAM,SysInfo,Process,CustomUser
# Create your views here.

class HelloView(APIView):
  
    def get(self,request):
        routes = [
        "GET /api -> To get all routes of api" ,
        "GET /api/ram -> To get all details of ram utilization",
        "GET /api/sys -> To get system information",
        "GET /api/prcs -> To get all process information",
        "GET /api/user -> To get all users", 

        ]
        return Response(routes)

class CustomUserView(APIView):
    def get(self,request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        print(request.data["password"])
        if serializer.is_valid():
            password = request.data["password"]
            password = make_password(password)
            request.data["password"] = password
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SysView(APIView):
    def get(self,request):
        sys = SysInfo.objects.all()
        serializer = SysSerializer(sys,many=True)
        return Response(serializer.data)
    
    def update(self,request, pk):
        data = request.data
        sys = SysInfo.objects.get(sys_id = pk)
        serializer = SysSerializer(
        instance=sys, data=data
    )
        if serializer.is_valid():
            serializer.save()

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



"""

data = {
"sysinfo":{
    "id": 1,
    "kernel_version": "12.03",
    "host_name": "Linux",
    "os_version": "kinetic",
    "cpu_count": 12,
    "cpus": {
        "key": "value",
        "key2": "value2"
    },
    "temp": {
        "temp1": "69"
    },
    "name": 2
} ,

"raminfo": {
sys_id
used_memory
total_memory
used_swap
total_swap
},

"prcs": ,
    
}

"""


class MasterView(APIView):
    def post(self,request):
        data = request.data

        sysinfo = data["sysinfo"]
        raminfo = data["raminfo"]

        prcs = data["prcs"]

        sys_serializer = SysSerializer(data=sysinfo)
        ram_serializer = RAMSerializer(data=raminfo)
        prcs_serializer = ProcessSerializer(data=prcs,many=True)

        if sys_serializer.is_valid() and ram_serializer.is_valid() and prcs_serializer.is_valid():
            sys_serializer.save()
            ram_serializer.save()
            prcs_serializer.save()
            return Response("Data saved successfully",status=status.HTTP_201_CREATED)
        return Response("Data not saved",status=status.HTTP_400_BAD_REQUEST)
    
