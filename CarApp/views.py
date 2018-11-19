from django.shortcuts import render
from . import models
from . import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import commands

# Create your views here.

commands_obj = commands.Commands()


class MotorCommands(generics.ListAPIView):
    def post(self, request, *args, **kwargs):
        try:
            command = request.data.get("command")
            commands_obj.execute(command)
            return Response({"CarStatus": commands_obj.status})
        except commands_obj.CommandNotFound as ex:
            return Response({"Error": ex})
        except Exception as ex:
            return Response({"Error": "Unknown Error: {0}".format(ex)})
