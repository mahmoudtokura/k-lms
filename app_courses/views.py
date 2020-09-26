from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = "course_list"
    template_name = "app_courses/course_list.html"

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "app_courses/course_detail.html"
