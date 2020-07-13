from django.db import models

from django.contrib.auth.models import User


class User_Register(models.Model):
    work_choice=(
        ('student','Student'),
        ('entrepreneur','Entrepreneur'),
        ('businessman',"Businessman"),
    )
    join_startup_as=(
        ('cofounder','Cofounder'),
        ('team member','Team member'),
        ('partner','Partner'),

    )
    lookinfor_choice=(
        ('startup idea','Startup Idea'),
        ('startup company',('Startup Company')),
    )
    picture=models.FileField(upload_to = 'media/',null=True,blank=True)

    name = models.OneToOneField(User, on_delete=models.CASCADE)

    Looking_for=models.CharField(max_length=50,choices=lookinfor_choice)
    Studies_or_Work_at=models.TextField(max_length=200)
    #Skills=models.

    email= models.EmailField(max_length=50)
    contact= models.CharField(max_length=20)
    address=models.TextField(max_length=200)
    I_am=models.CharField(max_length=50,choices=work_choice)
    industry=models.CharField(max_length=100)
    join_as=models.CharField(max_length=50,choices=join_startup_as)
    resume=models.FileField(upload_to='media/',null=True,blank=True)
    experience=models.CharField(max_length=50)
    about=models.TextField()

    College=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    Passing_year=models.CharField(max_length=100)
    percentage=models.IntegerField(max_length=6)
    company_name=models.CharField(max_length=100)
    job_post=models.CharField(max_length=100)
    duration=models.IntegerField(max_length=3)
    
    

    def __str__(self):
        return str(self.name)



