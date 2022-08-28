from django.shortcuts import render
from codify.models import Course
import json
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def course_list_api(request):
    courses = Course.objects.all()
    serializers_courses = serializers.serialize("json", list(courses))
    return JsonResponse(serializers_courses, safe=False)
