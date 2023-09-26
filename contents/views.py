from .models import Content
from courses.models import Course
from .serializers import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminUser, IsAdminOrOwner
from django.shortcuts import get_object_or_404
from rest_framework import generics


class ContentView(generics.CreateAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):

        course = get_object_or_404(Course, id=self.kwargs["course_id"])
        serializer.save(course=course)


class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]
