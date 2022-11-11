from django.shortcuts import render

# Create your views here.

def doctorhome(request):
    return render(request,'doctor_template/doctorhome.html')

def home(request):
    return render(request,'doctor_template/home.html')

def doctor(request):
    return render(request,'doctor_template/doctor.html')

def doctor_login(request):
    return render(request,'doctor_template/login.html')

def doctor_resetpassword(request):
    return render(request,'doctor_template/resetpassword.html')

def doctor_single(request):
    return render(request,'doctor_template/doctor-single.html')

def doctor_profile(request):
    return render(request,'doctor_template/profile.html')

def doctor_bootstrapeg(request):
    return render(request,'doctor_template/bootstrapeg.html')   

def doctor_edit_profile(request):
    return render(request,'doctor_template/edit_profile.html')       

def doctor_index(request):
    return render(request,'doctor_template/index.html') 

def doctor_department(request):
    return render(request,'doctor_template/department.html')      

def doctor_heartcare(request):
    return render(request,'doctor_template/heartcare.html')     

def doctor_womencare(request):
    return render(request,'doctor_template/womencare.html')      

def doctor_childcare(request):
    return render(request,'doctor_template/childcare.html')   

def neuroscience(request):
    return render(request,'doctor_template/neuroscience.html')    

def doctor_liver(request):
    return render(request,'doctor_template/liver.html')  

def orthopaedics(request):
    return render(request,'doctor_template/orthopaedics.html')   

def renalcare(request):
    return render(request,'doctor_template/renalcare.html')  

def endocrine(request):
    return render(request,'doctor_template/endocrine.html')    

def psychiarty(request):
    return render(request,'doctor_template/psychiarty.html')       

def oncology(request):
    return render(request,'doctor_template/oncology.html')         

def anaesthesiology(request):
    return render(request,'doctor_template/anaesthesiology.html')    

def radiology(request):
    return render(request,'doctor_template/radiology.html')    

def dermatology(request):
    return render(request,'doctor_template/dermatology.html')   

def bloodbank(request):
    return render(request,'doctor_template/bloodbank.html')

def contact(request):
    return render(request,'doctor_template/contact.html') 

def master(request):
    return render(request,'doctor_template/masterdepartment.html')  

def departmentsingle(request):
    return render(request,'doctor_template/departmentsingle.html')      


   

           