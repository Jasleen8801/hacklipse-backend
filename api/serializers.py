from rest_framework.serializers import ModelSerializer

from .models import RAM,CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','name','password']
        extra_kwargs = {'password': {'write_only': True}}

class RAMSerializer(ModelSerializer):
    class Meta:
        model = RAM
        fields = "__all__"
        exclude = []