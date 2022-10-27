from django.urls import path
from .import views

urlpatterns=[

    path('index',views.homepage_index),
    path('appoinment',views.homepage_appoinment),
    path('about',views.homepage_about),
    path('blogside',views.homepage_blogside),
    path('blogsingle',views.homepage_blogsingle),
    path('confirmation',views.homepage_confirmation)

]