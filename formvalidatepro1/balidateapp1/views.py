from django.shortcuts import render
from django.shortcuts import redirect
from .forms import EmployeeForm
from balidateapp1.models import Employee
from django.http.response import HttpResponse

def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})




