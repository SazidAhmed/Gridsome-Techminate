from django.shortcuts import render
from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Project, Team
from .serializers import ProjectSerializer, TeamSerializer

class ProjectList(APIView):
    def get(self, request, format=None):
        data = Project.objects.all()
        serializer = ProjectSerializer(data, many=True)
        return Response(serializer.data)


class TeamList(APIView):
    def get(self, request, format=None):
        data = Team.objects.all()
        serializer = TeamSerializer(data, many=True)
        return Response(serializer.data)
