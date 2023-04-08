from rest_framework.serializers import ModelSerializer

from .models import RAM

class RAMSerializer(ModelSerializer):
    class Meta:
        model = RAM
        fields = "__all__"
        exclude = []