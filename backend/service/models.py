from django.db import models
from user.models import User
from client.models import Client
from utils.utils import gen_random_filename

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=150, blank=False)
    type = models.CharField(max_length=50, choices=[("Individual", "Individual"), ("Group", "Group")], blank=False)
    location = models.CharField(max_length=150, blank=False)
    duration = models.TimeField()
    category = models.CharField(max_length=150, blank=False)
    staff_associated = models.ManyToManyField(User)
    client_associated = models.ManyToManyField(Client)
    image = models.ImageField(default="service_default.jpg", upload_to=gen_random_filename, blank=True)