from django.db import models


class FeedbcckData(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    email=models.EmailField(max_length=50)
    feedback=models.CharField(max_length=500)
