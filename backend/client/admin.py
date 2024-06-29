from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientAllergy)
admin.site.register(Allergy)
admin.site.register(ClientMedHist)
