from django.db import models
import datetime
# Create your models here.
class Task(models.Model):
    def __str__(self):#to make visible the name which we guve in admin pannel
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)