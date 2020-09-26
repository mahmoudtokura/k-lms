from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course'),
]