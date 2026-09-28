from django.urls import path
from . views import (
    ProjectsView,
     SkillsView,ProfileImagesView
)


urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('skills/', SkillsView.as_view(), name='projects_inquiry'),
    path('profileimages/',ProfileImagesView.as_view(), name='profile_images')
]