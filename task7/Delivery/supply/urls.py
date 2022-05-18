from django.urls import path
from supply import views

app_name = 'supply'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/?P<str:role>/',views.userlogin, name='login'),
    path('register/?P<str:role>/',views.register, name='register'),
    path('productsadd/', views.productsadd, name='productsadd'),
    path('dhome/',views.dashboardmanhome,name='dhome'),
    path('dashboarduser/', views.dashboarduser, name='dashboarduser'),
    path('manprofile/<manager_id>/',views.managerprofile, name='manprofile'),

]