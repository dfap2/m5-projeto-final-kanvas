from .models import Course
from students_courses.models import StudentCourse
from accounts.models import Account
from students_courses.serializers import StudentCourseSerializer
from .serializers import CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminOrReadOnly, IsAdminOrOwner, IsAdminUser
from rest_framework import generics
from django.shortcuts import get_object_or_404
import ipdb


class CourseView(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):

        if "instructor" in serializer.validated_data:

            serializer.save(instructor=serializer.validated_data["instructor"])
        else:
            serializer.save()


class CourseDetailVIew(generics.RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]


class StudentCourseView(generics.RetrieveUpdateAPIView):

    # ipdb.set_trace()

    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    lookup_field = "course_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):

        ipdb.set_trace()

        course = get_object_or_404(Course, pk=self.kwargs["course_id"])
        student = get_object_or_404(
            Account, email=self.request.students_course.student_email)

        serializer.save(course=course, student=student)
