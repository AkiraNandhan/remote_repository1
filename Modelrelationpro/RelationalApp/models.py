from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=100)
    sloc=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return self.sname

class Courses(models.Model):
    student=models.OneToOneField(Student,on_delete=models.SET(6),null=True)
    cname=models.CharField(max_length=100)
    cfee=models.IntegerField()
    institute=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
