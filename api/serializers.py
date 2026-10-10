from rest_framework import serializers
from . models import (
    Projects,
    Skills,
    ProfileImages
)


class ProfileImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model= ProfileImages
        fields = 'image_url'
        
        
    def get_image_url(self,obj):
        return obj.image.url
  
        
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        
   

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
        
