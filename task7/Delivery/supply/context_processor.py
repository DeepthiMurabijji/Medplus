from .models import *

def extras (request):
    man = Manager.objects.all()
    return {'man': man}