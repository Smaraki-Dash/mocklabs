from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    cources=[
        ('Python Fullstack Development', 'Python Fullstack Development'),
        ('Java Fullstack Development', 'Java Fullstack Development'),
        ('MERN Fullstack Development', 'MERN Fullstack Development'),
        ('Fullstack Development', 'Fullstack Development')
    ]
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    pno=models.CharField(max_length=200)
    add=models.TextField()
    course=models.CharField(max_length=200, choices=cources, default='Python Fullstack Development')
    profile_pic=models.ImageField(upload_to='students_profiles/')
    resume=models.FileField(upload_to='students_resumes')

    def __str__(self):
        return self.username.username