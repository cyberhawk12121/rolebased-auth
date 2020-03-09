from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, DoctorRegisterForm, PatientRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .decorators import patient_required, doctor_required
from django.views.generic import (
    TemplateView, 
    View, 
    CreateView, 
    DeleteView, 
    DetailView, 
    ListView,
    UpdateView,
    )
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

# HOME PAGE
def index(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctorHome')
        else:
            return redirect('patientHome')
    else:
        # user= CustomUser.objects.all()
        return render(request, 'authentica/index.html')

#patient Home page after login
@login_required
@patient_required
def patientHome(request):
    return render(request,'authentica/patienthome.html')

#doctor home page after login
@login_required
@doctor_required
def doctorHome(request):
    return render(request, 'authentica/doctorhome.html')

# DOCTOR REGISTRATION
class Doctor_registration(TemplateView):
    template_name = 'authentica/doctor_registration.html'
    model = CustomUser
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    def get(self, request):
        user= request.user
        if user.is_authenticated:
            return redirect('home')
        else:
            form = DoctorRegisterForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.POST:
            form = DoctorRegisterForm(request.POST)
            if form.is_valid():
                # instance= form.save(commit=False)
                form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')
                user = authenticate(email=email ,password=password) #django built in authentication
                login(request, user)
                return redirect('doctor-home') 
        else:
            form = DoctorRegisterForm()
        return render(request, self.template_name, {'form': form})

    

class Patient_registration(TemplateView):
    template_name = 'authentica/patient_registration.html'
    model = CustomUser
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    def get(self, request):
        user= request.user
        if user.is_authenticated:
            return redirect('home')
        else:
            form = PatientRegisterForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.POST:
            form = PatientRegisterForm(request.POST)
            if form.is_valid():
                # instance= form.save(commit=False)
                form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')
                user = authenticate(email=email ,password=password) #django built in authentication
                login(request, user)
                return redirect('patient-home') 
        else:
            form = PatientRegisterForm()
        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
    template_name= 'authentica/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form= LoginForm()
            return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.POST:
            form= LoginForm(request.POST)
            if form.is_valid():
                email= form.cleaned_data.get('email')
                password= form.cleaned_data.get('password')
                print(email, password)
                user= authenticate(email= email, password= password)
                if user is not None:
                    if user.is_doctor:
                        login(request, user)
                        return redirect('doctor-home')
                    else:
                        return redirect('patient-home')
        else:
            form= LoginForm()
        return render(request, self.template_name, {'form':form})


#Patient Authentication

def logout_view(request):
    if request.POST:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')
