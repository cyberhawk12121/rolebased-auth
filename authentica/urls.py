from django.urls import path
from . import views

urlpatterns= [
    #Home
    path('', views.index, name='home'),
    
    #Doctor (SuperUser)
    path('doctor/register/', views.Doctor_registration.as_view(), name='doctor-register'),
    path('account/doctor', views.doctorHome, name='doctor-home'),
    path('account/patient', views.patientHome, name='patient-home'),
    path('account/doctor', views.doctorHome, name='doctor-home'),
    #Patient
    path('patient/register/', views.Patient_registration.as_view(), name='patient-register'),
    path('login/', views.LoginView.as_view(), name='login'),

    #Logout
    path('logout/', views.logout_view, name='logout'),
]