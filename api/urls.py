from django.urls import path
from . views import (
    ProjectsView,
     SkillsView
)


urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('skills/', SkillsView.as_view(), name='projects_inquiry'),
]



