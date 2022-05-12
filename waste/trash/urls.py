
from django.urls import path
from trash import views
from .views import * 

app_name = 'trash'

urlpatterns = [
    path('', home, name='home'),
    path('reg/', registeration, name='reg'),
    path('signin/', signin, name='signin'),
]