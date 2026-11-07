from django.shortcuts import render
from .serializers import (
    ProjectsSerializer,
    ProfileImagesSerializer,
    SkillsSerializer,
)
from .models import Projects, Skills, ProfileImages
from rest_framework.response import Response
from rest_framework.views import APIView, csrf_exempt
from rest_framework import status


import json
from django.http import JsonResponse
from django.conf import settings
import os 
import requests
# from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)
import resend
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
"""
class SendMessage(APIView):
    def post(self, request):
        try:
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            message = request.data.get("message")

            subject = (f"Portfolio message from {first_name} {last_name}",)
            message = (f"Message: {message}",)
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.RECIPIENT_EMAIL],
                fail_silently=False,
            )

            return Response({"success": True})

        except Exception as e:
            return Response(
                {"success": False, "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

"""


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

resend.api_key = os.getenv("RESEND_API_KEY")
@api_view(['POST'])
@permission_classes([AllowAny])
def send_email(request):
    if request.method == "POST":
            data = json.loads(request.body)
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            message = data.get("message")
            email = data.get("email")
          
            if not all([first_name,last_name,message]):
                return JsonResponse({'Error': "Please fill out all fields"}, status=status.HTTP_400_BAD_REQUEST)
        
            recipient = settings.RECIPIENT_EMAIL


            # Composing the email
            subject = f"New Contact Message from {first_name} {last_name}"
            email_message = f"Name: {first_name} {last_name}\nEmail: {email} \n\n Message:\t{message}"

            # Send email funtion
            try:
                resend.Emails.send({
                    "from": "onboarding@resend.dev",
                    "to": recipient,
                    "subject": subject,
                    "text": email_message
                })
                
                return JsonResponse({"success": "Message sent successfully!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({"error": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
