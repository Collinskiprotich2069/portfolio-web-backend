from django.shortcuts import render
from . serializers import (
    ProjectsSerializer,
    ProfileImagesSerializer,
    SkillsSerializer,
    
)
from . models import (
    Projects,
    Skills,
    ProfileImages
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
    
class ProfileImagesView(APIView):
    def get(self,request):
        model = ProfileImages.objects.all()
        serializer = ProfileImagesSerializer(model, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ProjectsView(APIView):
    #http_method_names = ['get']
    
    def get(self, request):
        model = Projects.objects.all()
        serializer = ProjectsSerializer(model, many=True, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SkillsView(APIView):
    http_method_names = 'get'
    def get(self, request):
        model = Skills.objects.all()
        serializer = SkillsSerializer(model, many=True,context={'request':request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    