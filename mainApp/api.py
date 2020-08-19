from rest_framework import generics, status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    class Meta:
        model = models.CustomUser
        fields = '__all__'

    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class MetaDataListView(generics.ListCreateAPIView):
    serializer_class = serializers.MetaDataSerializer

    class Meta:
        model = models.MetaData
        fields = ('name', 'value',)

    def get_queryset(self):
        if 'name' in self.kwargs:
            qs = models.MetaData.objects.filter(user=self.request.user, name=self.kwargs['name'])
        else:
            qs = models.MetaData.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DocumentsListView(generics.ListCreateAPIView):
    serializer_class = serializers.DocumentsSerializer

    class Meta:
        model = models.Documents
        fields = ('name', 'file',)

    def get_queryset(self):
        if 'name' in self.kwargs:
            qs = models.Documents.objects.filter(user=self.request.user, name=self.kwargs['name'])
        else:
            qs = models.Documents.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(name=self.request.data['file'], user=self.request.user)

    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        print(request.data)
        if 'file' not in request.data:
            raise ParseError("No file found")

        f = request.data['file']

        models.Documents.file.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)
