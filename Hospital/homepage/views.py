from django.shortcuts import render

# Create your views here.

def homepage_index(request):
    return render(request,'homepage_template/index.html')

    