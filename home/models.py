from django.db import models
from tinymce import models as tinymce_models
class Home(models.Model):
    salutation=models.CharField(max_length=200)
    skills1=models.CharField(max_length=200, blank=True)
    skills2=models.CharField(max_length=200,blank=True)
    skills3=models.CharField(max_length=200, blank=True)
    skills4=models.CharField(max_length=200,blank=True)
    desc=tinymce_models.HTMLField()
    your_image=models.ImageField(upload_to="media")
class about(models.Model):
    about_you=tinymce_models.HTMLField()
    email=models.EmailField()
    Date_of_Birth=models.DateField(blank=True)
    Phone=models.CharField(max_length=10)
    website=models.CharField(max_length=50, blank=True)
    Degree=models.CharField(max_length=50, blank=True)
    sex=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    Resume=models.FileField(upload_to="media")
class skills(models.Model):
    skill_No=models.IntegerField()
    skills_title=models.CharField(max_length=50)
    konwledge_percentage=models.IntegerField()
class education(models.Model):
    course_name=models.CharField(max_length=100)
    course_desc=tinymce_models.HTMLField()
    strt_year1=models.CharField(max_length=4)
    end_year1=models.CharField(max_length=4)
class experience(models.Model):
    exp_title=models.CharField(max_length=500)
    strt_year=models.CharField(max_length=4)
    end_year=models.CharField(max_length=4)
    exp_desc=tinymce_models.HTMLField()
class services(models.Model):
    choic=(("fa fa-mobile-alt","mobile_icon"),("fa fa-bullhorn","icon2"),("fa fa-search","search_icon"),("fa fa-code","code_icon"),("fa fa-palette","icon4"),("fa fa-laptop-code","icon5"))
    category=models.CharField(max_length=50,choices=choic)
    service_title=models.CharField(max_length=100)
    service_desc=models.TextField()
class projects(models.Model):
    Portfolio_picture=models.ImageField(upload_to="media")
    links=models.CharField(max_length=150)
class contact(models.Model):
    email_id=models.EmailField()
    contact_no=models.CharField(max_length=10)
    website_name=models.CharField(max_length=50)
    office=models.CharField(max_length=100)
class Messages(models.Model):
    username=models.CharField(max_length=50)
    user_mail_id=models.EmailField()
    Subject=models.CharField(max_length=200)
    content=models.TextField()
    
# Create your models here.
