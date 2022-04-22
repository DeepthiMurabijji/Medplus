from unicodedata import name
from django.urls import path 

from base import views

app_name = "base"

urlpatterns = [ 
    path('',views.home, name='home'),
    #path('',views.index, name='index'),
    # path('ppl/',views.people_view, name='people'),
    # path('formpage/', views.form_name, name='form_name'),
]