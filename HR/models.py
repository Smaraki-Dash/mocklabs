from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ratings(models.Model):
    sub=[
        ('python', 'python'),
        ('java', 'java'),
        ('django', 'django'),
        ('spring boot' , 'spring boot' ),
        ('Hibernate', 'Hibernate'),
        ('React js', 'React js'),
        ('Mern', 'Mern'),
        ('Node JS', 'Node JS'),
        ('Next js','Next js'),
        ('Webtech', 'Webtech')
    ]   
    raatings=[
        ('*', '*'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    student=models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    subjects=models.CharField(max_length=50, choices=sub, default='python')
    communication=models.CharField(max_length=50, choices=raatings, default='1')
    technical=models.CharField(max_length=50, choices=raatings, default='1')
    programming=models.CharField(max_length=50, choices=raatings, default='1')
    remarks=models.CharField(max_length=200)
    conducted_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='by')
    conducted_on=models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.student.username