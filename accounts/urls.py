from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('candidat_register/',views.candidat_register.as_view(), name='candidat_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]