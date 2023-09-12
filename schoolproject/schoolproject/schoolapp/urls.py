from django.contrib import admin
from django.urls import path, include
from . import views
app_name='school'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('submit',views.submit,name='submit'),
    path('register/',views.register,name='register'),
    path('hello/',views.hello,name='hello'),
    path('form_order',views.form_order,name='form_order')
]