from django.shortcuts import render

# Create your views here.

def homepage_index(request):
    return render(request,'homepage_template/index.html')

def homepage_appoinment(request):
    return render(request,'homepage_template/appoinment.html')

def homepage_about(request):
    return render(request,'homepage_template/about.html')

def homepage_blogside(request):
    return render(request,'homepage_template/blog-sidebar.html')  

def homepage_blogsingle(request):
    return render(request,'homepage_template/blog-single.html')

def homepage_confirmation(request):
    return render(request,'homepage_template/confirmation.html')

    










