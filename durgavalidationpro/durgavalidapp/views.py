from django.shortcuts import render

from durgavalidapp.forms import FeedbackForm,SignupForm

def feedback_form_view(request):
    form=FeedbackForm()
    if request.method=='POST':
        form =FeedbackForm(request.POST)
        if form.is_valid():
            print('basic validation is completed')
            print('Name',form.cleaned_data['name'])
            print('Rollno',form.cleaned_data['rollno'])
            print('Email',form.cleaned_data['email'])
            print('Feedback',form.cleaned_data['feedback'])
    return render(request,'durgavalidapp/feedback.html',{'form':form})

def Signup_form_view(request):
    form =SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('basic validation is completed and printing data ')
            print('Name',form.cleaned_data['name'])
            print('Password',form.cleaned_data['password'])
            print('Email',form.cleaned_data['email'])
    return render(request,'durgavalidapp/signup.html',{'form':form})
