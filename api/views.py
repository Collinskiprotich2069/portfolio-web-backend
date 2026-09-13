from django.shortcuts import render
from . serializers import (
    ProjectsSerializer,
    SkillsSerializer
)
from . models import (
    Projects,
    Skills
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
    

class ProjectsView(APIView):
    #http_method_names = ['get']
    
    def get(self, request):
        model = Projects.objects.all()
        serializer = ProjectsSerializer(model, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SkillsView(APIView):
    http_method_names = 'get'
    def get(self, request):
        model = Skills.objects.all()
        serializer = SkillsSerializer(model, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    