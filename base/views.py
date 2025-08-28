from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, BasicConfiguration, Resume, About

# Create your views here.

def basic_configuration(request):
    try:
        basic_conf_obj = BasicConfiguration.objects.all().order_by('-id')[0]

        basic_conf_dict = {
            'logo_dark': f"{request.scheme}://{request.get_host()}{basic_conf_obj.logo_dark.url}",
            'logo_light': f"{request.scheme}://{request.get_host()}{basic_conf_obj.logo_light.url}",
            'your_photo': f"{request.scheme}://{request.get_host()}{basic_conf_obj.your_photo.url}",
            'your_name': basic_conf_obj.your_name,
            'your_designation': basic_conf_obj.your_designation,
            'youtube_link': basic_conf_obj.youtube_link,
            'instagram_link': basic_conf_obj.instagram_link,
            'github_link': basic_conf_obj.github_link,
            'gmail_link': basic_conf_obj.gmail_link,
            'linkedin_link': basic_conf_obj.linkedin_link,
            'your_years_of_experience': basic_conf_obj.your_years_of_experience,
            'your_number_of_satisfied_clients': basic_conf_obj.your_number_of_satisfied_clients,
            'your_number_of_completed_projects': basic_conf_obj.your_number_of_completed_projects
        }

        return JsonResponse({'ok': 200, 'basic_conf': basic_conf_dict})

    except:
        return JsonResponse({'ok': 500, 'basic_conf': {}})

def get_resume(request):
    try:
        resume_obj = Resume.objects.all().order_by('-id')[0]

        resume_dict = {
            'resume_file': f"{request.scheme}://{request.get_host()}{resume_obj.resume_file.url}"
        }

        return JsonResponse({'ok': 200, 'resume': resume_dict})

    except:
        return JsonResponse({'ok': 500, 'resume': {}})

def get_projects(request):
    try:
        all_projects = Project.objects.all().order_by('-id')

        projects_list = [

            {
                'id': project.id,
                'title': project.title,
                'image_url': f"{request.scheme}://{request.get_host()}{project.image.url}",
                'details': project.details,
                'categories': [category.category_name for category in project.categories.all()]
            }

            for project in all_projects

        ]

        return JsonResponse({'ok': 200, 'projects': projects_list})

    except:
        return JsonResponse({'ok': 500, 'projects': []})

def get_single_project_details(request, project_id):
    try:
        project_object = Project.objects.get(id=project_id)

        project_dict = {
            'id': project_object.id,
            'title': project_object.title,
            'image_url': f"{request.scheme}://{request.get_host()}{project_object.image.url}",
            'details': project_object.details,
            'categories': [category.category_name for category in project_object.categories.all()]
        }

        return JsonResponse({'ok': 200, 'project': project_dict})

    except:
        return JsonResponse({'ok': 500, 'project': {}})

def get_about_info(request):
    try:
        about_info_obj = About.objects.all().order_by('-id')[0]

        about_info_dict = {
            'intro': about_info_obj.intro,
            'work_experiences': [{'title': work_experience.title, 'work_duration': work_experience.work_duration, 'company_name': work_experience.company_name, 'description': work_experience.description} for work_experience in about_info_obj.work_experiences.all()] if about_info_obj.work_experiences else [],
            'educations': [{'education_duration': education.education_duration, 'title': education.title, 'university_name': education.university_name} for education in about_info_obj.educations.all()] if about_info_obj.educations else [],
            'hard_skills': [{'skill_image': f"{request.scheme}://{request.get_host()}{hard_skill.skill_image.url}", 'number_of_projects': hard_skill.number_of_projects, 'title': hard_skill.title} for hard_skill in about_info_obj.hard_skills.all()] if about_info_obj.hard_skills else [],
            'soft_skills': [{'title': soft_skill.title} for soft_skill in about_info_obj.soft_skills.all()] if about_info_obj.soft_skills else []
        }

        return JsonResponse({'ok': 200, 'about_info': about_info_dict})

    except:
        return JsonResponse({'ok': 500, 'about_info': {}})