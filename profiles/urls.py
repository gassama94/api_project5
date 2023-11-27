from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),

    # Project URLs
    path('api/projects/', views.ProjectList.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),

    # Task URLs
    # path('api/tasks/', views.TaskList.as_view(), name='task-list'),
    path('api/projects/<int:project_id>/tasks/', views.TaskList.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]
