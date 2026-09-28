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
        
    def get_image(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.get_absolute_uri(obj.image.url)
        return None
        
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
        
    def get_image(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None