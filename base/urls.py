from django.urls import path
from . import views

urlpatterns = [
    path('basic-configuration', views.basic_configuration, name='basic-configuration'),
    path('resume', views.get_resume, name='resume'),
    path('projects', views.get_projects, name='projects'),
    path('projects/<int:project_id>', views.get_single_project_details, name='project-details'),
    path('about-info', views.get_about_info, name='about-info')
]