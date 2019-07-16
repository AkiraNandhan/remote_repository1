from django.contrib import admin
from .models import Student,Courses

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','sloc','email']

class AdminCourses(admin.ModelAdmin):
    list_display = ['cname','cfee','institute']

admin.site.register(Student,AdminStudent)
admin.site.register(Courses,AdminCourses)