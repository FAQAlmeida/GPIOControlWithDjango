from django.shortcuts import render
from . import models
from . import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class GPIOPinView(APIView):
    def get_object(self, pk):
        try:
            return models.GPIOPin.objects.get(pk=pk)
        except models.GPIOPin.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        snippets = models.GPIOPin.objects.all()
        serializer = serializers.GPIOPinSerializer(snippets, many=True)
        return JsonResponse(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.GPIOPinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
