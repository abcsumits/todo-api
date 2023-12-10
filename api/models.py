from django.db import models
from datetime import date
class todo_item(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=1000,default="")
    due_date=models.DateField(default=date(9999,12,31))
    tag=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default="OPEN")
    username=models.CharField(max_length=100,default="")
    