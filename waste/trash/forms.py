
from django import forms
from django.contrib.auth.models import User
from trash.models import *


class registerationform(forms.ModelForm):
    class Meta():
        model= User
        fields = ['first_name','last_name','email','username','password']