from rest_framework import serializers
from . models import (
    Projects,
    Skills,
    ProfileImages
)


class ProfileImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProfileImages
        fields = '__all__'
        
  
        
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        
   

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
        
