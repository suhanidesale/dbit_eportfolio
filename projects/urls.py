from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    
    path('create-project/', views.createProject, name= "create-project"),
    path('update-project/<str:pk>/' , views.updateeProject,name="update-project"),
    path('delete-project/<str:pk>/' , views.deleteProject,name="delete-project"),
    path('', views.internships, name="internships"),
    path('internship/<str:pk>/', views.internship, name="internship"),
    path('create-internship/', views.createinternship, name= "create-internship"),
 
]
