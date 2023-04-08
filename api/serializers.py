from rest_framework.serializers import ModelSerializer

from .models import RAM,CustomUser,SysInfo,Process

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','name','password']
        extra_kwargs = {'password': {'write_only': True}}

class SysSerializer(ModelSerializer):
    class Meta:
        model = SysInfo
        fields = "__all__"
        exclude = []

class RAMSerializer(ModelSerializer):
    class Meta:
        model = RAM
        fields = "__all__"
        exclude = []

class ProcessSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"
        exclude = []