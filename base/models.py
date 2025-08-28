from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class BasicConfiguration(models.Model):
    logo_dark = models.ImageField(upload_to = 'logos', null = True, blank = True)
    logo_light = models.ImageField(upload_to = 'logos', null = True, blank = True)
    your_photo = models.ImageField(upload_to='user_images', null = True, blank = True)
    your_name = models.CharField(max_length = 150, null = True, blank = True)
    your_designation = models.CharField(max_length = 100, null = True, blank = True)
    youtube_link = models.CharField(max_length = 200, null = True, blank = True, help_text = 'The link must start with "http:// or https://"')
    instagram_link = models.CharField(max_length = 200, null = True, blank = True, help_text = 'The link must start with "http:// or https://"')
    github_link = models.CharField(max_length = 200, null = True, blank = True, help_text = 'The link must start with "http:// or https://"')
    gmail_link = models.CharField(max_length = 200, null = True, blank = True, help_text = 'The link must start with "http:// or https://"')
    linkedin_link = models.CharField(max_length = 200, null = True, blank = True, help_text = 'The link must start with "http:// or https://"')
    your_years_of_experience = models.FloatField(null = True, blank = True)
    your_number_of_satisfied_clients = models.FloatField(null = True, blank = True)
    your_number_of_completed_projects = models.FloatField(null = True, blank = True)

    def __str__(self):
        return f'{self.your_name} - {self.your_designation}'

class Resume(models.Model):
    resume_file = models.FileField(
        upload_to="resumes/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
    )

    def __str__(self):
        return f'Resume file - {self.id}'

class ProjectCategory(models.Model):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Project categories'


class Project(models.Model):
    title = models.CharField(max_length = 200)
    categories = models.ManyToManyField(ProjectCategory)
    details = models.TextField()
    image = models.ImageField(upload_to = 'project_images', null = True, blank = True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    title = models.CharField(max_length = 150)
    work_duration = models.CharField(max_length = 30)
    company_name = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    education_duration = models.CharField(max_length = 30)
    title = models.CharField(max_length = 250)
    university_name = models.CharField(max_length = 300)

    def __str__(self):
        return self.title

class HardSkill(models.Model):
    skill_image = models.ImageField(upload_to = 'skill_images')
    number_of_projects = models.IntegerField()
    title = models.CharField(max_length = 150)

class SoftSkill(models.Model):
    title = models.CharField(max_length = 300)

    def __str__(self):
        return self.title

class About(models.Model):
    intro = models.TextField(null = True, blank = True)
    work_experiences = models.ManyToManyField(WorkExperience)
    educations = models.ManyToManyField(Education)
    hard_skills = models.ManyToManyField(HardSkill)
    soft_skills = models.ManyToManyField(SoftSkill)

    def __str__(self):
        return f"{self.intro[:10]}..."

    class Meta:
        verbose_name_plural = 'About'
