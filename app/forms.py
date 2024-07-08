from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class CustomrUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'gender', 'user_type', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

class customAuthForm(AuthenticationForm):
    class Meta: 
        model = CustomUser
        fields = ("username", 'password')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class jobinfoForm(forms.ModelForm):
    class Meta:
        model = JobInfo
        fields = ['job_title','industry','application_deadline','specific_gender','job_description','academic_qualifications','job_requirements','salary','experience','job_skills','company_logo']

        widgets = {
            'application_deadline':forms.DateInput(attrs={'type':'date'})
        }
        
        