from django import forms


class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.CharField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('total form validation by using clean method..')
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if inputname[0].lower()!='d':
            raise forms.ValidationError('name should not starts with d|D')
        inputrollno=total_cleaned_data['rollno']
        if inputrollno <=0:
            raise forms.ValidationError('roll no should be > 0')
class SignupForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Reenter password',widget=forms.PasswordInput)
    email=forms.EmailField()

    def clean(self):
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError('Both passwords must be match')
