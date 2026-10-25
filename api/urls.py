from django.urls import path
from .views import ProjectsView, send_message_email, SkillsView, ProfileImagesView

urlpatterns = [
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("skills/", SkillsView.as_view(), name="projects_inquiry"),
    path("message/", send_message_email, name="send_message"),
    path("profileimages/", ProfileImagesView.as_view(), name="profile_images"),
]
