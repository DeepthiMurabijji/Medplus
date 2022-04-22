import email
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'students.settings')


import django
django.setup()

from base.models import people
from faker import Faker 

fakegen = Faker()


def populate(n=5):


    for entry in range(n):
        # fake_firstname = fakegen.FirstName()
        # fake_lastname = fakegen.LastName()
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        
        pep = people.objects.get_or_create(FirstName = fake_first_name,LastName = fake_last_name,email = fake_email)[0] 


if __name__=='__main__':
    print("populated")
    populate(20)
    print("complete!")

else :
    print("couldn't complete")