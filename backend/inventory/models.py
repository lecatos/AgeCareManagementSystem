from django.db import models
import datetime as dt
from utils.utils import gen_random_filename

# Create your models here.
class Inventory(models.Model):
    #id = None
    item_name = models.CharField(primary_key=True, max_length=150, blank=False)
    critical_point = models.IntegerField(blank=False)
    qty = models.PositiveIntegerField(blank=False)
    desc = models.CharField(max_length=150, blank=True)
    last_restock = models.DateField(auto_now_add=True)
    image = models.ImageField(default="inventory_default.jpg", upload_to=gen_random_filename, blank=True)
    
    @property
    def weekly_avg(self):
        last_week = dt.date.today() - dt.timedelta(days=7)
        his = InvHis.objects.filter(inventory=self, date__gte=last_week)
        return his

class InvHis(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(blank=False)
    date = models.DateField(auto_now_add=True)