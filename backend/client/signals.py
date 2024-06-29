from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import ClientAllergy, Allergy
 
 
@receiver([post_delete, post_save], sender=ClientAllergy) 
def update_delete_allergy(sender, instance, **kwargs):
    Allergy.objects.filter(clientallergy__isnull=True).delete()