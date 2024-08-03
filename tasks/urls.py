from django.urls import path
from . import views


urlpatterns = [
    path('task/', views.TaskListAPIView.as_view()),
    path('task/<int:id>/', views.TaskItemAPIView.as_view()),
]
