from django.db import models

class Employee(models.Model):
    eid=models.CharField(max_length=100)
    ename=models.CharField(max_length=100)
    econtact=models.CharField(max_length=100)
