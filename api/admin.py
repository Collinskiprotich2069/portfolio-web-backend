from django.contrib import admin
from .models import (
    Skills, 
    Projects,
    ProfileImages
)


admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(ProfileImages)