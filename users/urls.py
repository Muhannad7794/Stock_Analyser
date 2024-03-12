# users/urls.py
from django.urls import path, include  # include is added here for use with router.urls
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r"", UserProfileViewSet, basename="userprofile")

urlpatterns = [
    path("", include(router.urls)),  # This includes the URLs generated by the router
]