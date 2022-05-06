from email.policy import default
from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

choice_value = [('CSE','CSE'),('ECE','ECE'),('IT','IT')]
sec_value = [('A','A'),('B','B'),('C','C')]
year_value = [('1','1'),('2','2'),('3','3'),('4','4')]
class st_details(models.Model):
    name_validators = RegexValidator(regex='^[a-zA-Z]*$',message='Name must be Alphabets only',code='invalid_username')
    FirstName = models.CharField(validators = [name_validators], max_length=45,blank="")
    LastName = models.CharField(validators = [name_validators], max_length=45,blank="")


    rollno = models.CharField(validators=[RegexValidator('^[0-9]*$', message='Roll.no must be Numbers only'), ],max_length=4,help_text="Enter 4 digit roll number",blank="", unique= True)
    profilepic = models.ImageField(null=True ,blank=True ,upload_to ='uploads/', default="uploads/unknown.jpg")
    email = models.EmailField( max_length=265, unique=True,blank="")

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phoneno = models.CharField(validators=[phone_regex], max_length=10, blank=True) # Validators should be a list
    #phoneno =models.IntegerField(blank="",validators=[validators.MaxLengthValidator(10)])


    Year = models.CharField(max_length=2,choices=year_value,blank="")
    Branch = models.CharField(max_length=3,choices=choice_value,blank="")
    Section = models.CharField(max_length=2,choices=sec_value,blank="")

    def __str__(self) -> str:
        return self.rollno

def validate_interval(value):
        if value < 0.0 or value > 10.0:
            raise ValidationError(('%(value)s must be in the range [0.0, 10.0]'), params={'value': value},)




class Marks(models.Model):
    rollno = models.OneToOneField(st_details, on_delete = models.CASCADE)
    sem1 = models.FloatField (null=True, blank=True ,validators=[validate_interval])
    sem2 = models.FloatField (null=True, blank=True , validators=[validate_interval] )
    sem3 = models.FloatField (null=True, blank=True  , validators=[validate_interval])
    sem4 = models.FloatField (null=True, blank=True , validators=[validate_interval])
    sem5 = models.FloatField (null=True, blank=True , validators=[validate_interval])
    sem6 = models.FloatField (null=True, blank=True , validators=[validate_interval])
    sem7 = models.FloatField (null=True, blank=True , validators=[validate_interval])
    sem8 = models.FloatField (null=True, blank=True , validators=[validate_interval])

