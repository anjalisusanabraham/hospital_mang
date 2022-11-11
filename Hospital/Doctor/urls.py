from django.urls import path
from .import views

app_name ="home"

urlpatterns=[


    path('doctorhome',views.doctorhome),
    path('home',views.home),
    path('doctor',views.doctor),
    path('login',views.doctor_login),
    path('resetpassword',views.doctor_resetpassword),
    path('single',views.doctor_single),
    path('profile',views.doctor_profile),
    path('edit_profile',views.doctor_edit_profile),
    path('bootstrapeg',views.doctor_bootstrapeg),
    path('index',views.doctor_index),
    path('department',views.doctor_department),
    path('heartcare',views.doctor_heartcare),
    path('womencare',views.doctor_womencare),
    path('childcare',views.doctor_childcare),
    path('neuroscience',views.neuroscience),
    path('liver',views.doctor_liver),
    path('orthopaedics',views.orthopaedics),
    path('renalcare',views.renalcare),
    path('endocrine',views.endocrine),
    path('psychiarty',views.psychiarty),
    path('oncology',views.oncology),
    path('anaesthesiology',views.anaesthesiology),
    path('radiology',views.radiology),
    path('dermatology',views.dermatology),
    path('bloodbank',views.bloodbank),
    path('contact',views.contact),
    path('masterdepartment',views.master),
    path('departmentsingle',views.departmentsingle)
       

]