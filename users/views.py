from rest_framework import status, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # Allow non-authenticated users to register
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            user_profile = UserProfile.objects.create(
                user=user
            )  # Assuming default values are fine

            # Send confirmation email
            send_mail(
                "Confirm Your Registration",
                "Welcome! Please confirm your registration.",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            user_profile_serializer = UserProfileSerializer(user_profile)
            return Response(
                user_profile_serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
