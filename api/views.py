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


# Create your views here.

class HelloView(APIView):
  
    def get(self,request):
        routes = [
        "GET /api",
        
        ]
        return Response(routes)