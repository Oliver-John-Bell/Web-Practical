# models.py in your app directory
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
