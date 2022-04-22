import imp
from pyexpat import model
from attr import fields
from django import forms
from base.models import  *



# choice_value = [('CSE','CSE'),('ECE','ECE'),('IT','IT')]
# sec_value = [('A','A'),('B','B'),('C','C')]
# year_value = [('1','1'),('2','2'),('3','3'),('4','4')]
class newuser(forms.ModelForm):
    # Branch = forms.CharField(widget=forms.RadioSelect,choices=choice_value,blank="")
    # Year = forms.CharField(choices=year_value,blank="")
    # Section = forms.CharField(choices=sec_value,blank="")
    class Meta:
        model = st_details
        fields = '__all__'

class marksheet(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'
    
