from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
     #login view
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'),
        name='login'),

     # logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'),
        name='logout'),

    path('', Home.as_view(), name='home'),

    path('/report', Report.as_view(), name='report'),
    
]