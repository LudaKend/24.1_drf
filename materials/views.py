from django.shortcuts import render
from rest_framework import viewsets
from materials.models import Course
from materials.course_serializer import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# Create your views here.
