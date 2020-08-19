from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MetaData
        fields = ('name', 'value',)


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Documents
        fields = ('name', 'file',)
