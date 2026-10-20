from django.shortcuts import render
from .serializers import (
    ProjectsSerializer,
    ProfileImagesSerializer,
    SkillsSerializer,
)
from .models import Projects, Skills, ProfileImages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


import json
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


class ProfileImagesView(APIView):

    def get(self, request):
        model = ProfileImages.objects.all()
        serializer = ProfileImagesSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectsView(APIView):
    # http_method_names = ['get']

    def get(self, request):
        model = Projects.objects.all()
        serializer = ProjectsSerializer(model, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SkillsView(APIView):
    http_method_names = "get"

    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
def send_message_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            message = data.get("message")

            if not first_name or not last_name or not message:
                return JsonResponse({"error": "All fields are required."}, status=400)

            # Composing the email
            subject = f"New Contact Message from {first_name} {last_name}"
            email_message = f"Name: {first_name} {last_name}\n\nMessage:\n{message}"

            # Send email funtion
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ["collinskiprotich754@gmail.com"],
                fail_silently=False,
            )

            return JsonResponse({"success": "Email sent successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)
