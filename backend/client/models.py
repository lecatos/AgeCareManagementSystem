from django.db import models
from django.utils import timezone
from utils.utils import gen_random_filename
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    sex = models.CharField(max_length=1, choices=[("M", "M"), ("F", "F")], blank=False)
    dob = models.DateField(blank=False)
    email = models.EmailField(unique=False, blank=True)
    tel = models.CharField(max_length=20, unique=False, blank=True)
    avatar = models.ImageField(default="default.jpg", upload_to=gen_random_filename, blank=True)
    bio = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    @property
    def allergy(self):
        allergys = Allergy.objects.filter(clientallergy__client=self)
        return [allergy.allergy for allergy in allergys]
        
    @property
    def medhist(self):
        emedhist = ClientMedHist.objects.filter(client=self)
        return emedhist


#class ClientProfile(models.Model):
#    client = models.OneToOneField(Client, on_delete=models.CASCADE)
#    avatar = models.ImageField(default="default.jpg", upload_to="", blank=True)
#    bio = models.CharField(max_length=50, blank=True)
class Allergy(models.Model):
    id = None
    allergy = models.CharField(primary_key=True, max_length=50, blank=False)

    def save(self, *args, **kwargs):
        self.allergy = self.allergy.strip().capitalize()
        super().save(*args, **kwargs)

class ClientAllergy(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('client', 'allergy'),)

class ClientMedHist(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    facility = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False)

    class Meta:
        ordering = ['-date']
