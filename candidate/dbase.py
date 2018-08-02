from .models import *
from django.utils import timezone

def addCandidate(self, data):
    try:
        q = Candidate()
        q.name = data["name"]
        q.email = data["email"]
        q.address = data["address"]
        q.pincode = data["pincode"]
        q.experience = data["experience"]
        q.phone = data["phone"]
        q.cv_path = data["cv_path"]
        q.created_timestamp = timezone.now()
        q.save()
        return True
    except:
        return False

