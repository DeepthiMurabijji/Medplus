from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# class register(models.Model):
#     user=models.OneToOneField(User, on_delete = models.CASCADE)


#     def __str__(self) -> str:
#         return self.user.username



class Houses(models.Model):
    pass

class Areas(models.Model):
    pass

class Collector(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    



# Here we connect Collector with User using ONeToOneField