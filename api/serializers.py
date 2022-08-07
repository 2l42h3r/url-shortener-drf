from rest_framework.serializers import ModelSerializer
from .models import UrlList

class UrlListSerializer(ModelSerializer):
    class Meta:
        model = UrlList
        fields = '__all__'