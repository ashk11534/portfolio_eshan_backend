from django.contrib import admin
from .models import (ProjectCategory, Project, BasicConfiguration, Resume,
                     WorkExperience, Education, HardSkill, SoftSkill, About, Message,
                     Award, ResearchPaper, Course, Certificate, Achievement)

# Register your models here.

admin.site.register(BasicConfiguration)
admin.site.register(Resume)
admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(HardSkill)
admin.site.register(SoftSkill)
admin.site.register(About)
admin.site.register(Message)
admin.site.register(Award)
admin.site.register(ResearchPaper)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(Achievement)
