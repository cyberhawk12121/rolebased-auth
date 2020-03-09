from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from .models import CustomUser
from django.db import transaction
 

class DoctorRegisterForm(UserCreationForm):
    name= forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    speciality= forms.CharField(label="Speciality", widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.CharField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label="Password1", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label="Password1", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields= ('email', 'name', 'speciality')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = CustomUser.objects.create(user=user)
        doctor.name.add(*self.cleaned_data.get('name'))
        doctor.name.add(*self.cleaned_data.get('speciality'))
        user.is_superuser= True
        user.admin= True
        user.is_staff= True
        
        return user

class PatientRegisterForm(UserCreationForm):
    name= forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    illness= forms.CharField(label="Illness", widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.CharField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields= ('email',)
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.is_superuser= False
        user.admin= False
        user.is_staff= False
        if commit:
            user.save()
        return user




class LoginForm(forms.Form):
    email= forms.CharField(max_length=255, widget= forms.EmailInput)
    password= forms.CharField(max_length=255, widget=forms.PasswordInput)
    