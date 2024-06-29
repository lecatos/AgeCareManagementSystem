from django.db import models
from utils.utils import gen_random_filename
from django.contrib.auth.models import AbstractUser


#Create your own models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    sex = models.CharField(max_length=1, choices=[("M", "M"), ("F", "F")], blank=False)
    dob = models.DateField(blank=False)
    email = models.EmailField(unique=False, blank=True)
    tel = models.CharField(max_length=20, unique=False, blank=True)
    avatar = models.ImageField(default="default.jpg", upload_to=gen_random_filename, blank=True)
    bio = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = []

class Qualification(models.Model):
    id = None
    qualification = models.CharField(max_length=150, blank=False)

class StaffQualification(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('staff', 'qualification'),)

