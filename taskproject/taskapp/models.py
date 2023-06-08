from django.db import models

# # Create your models here.
class Task(models.Model):
    SL_No=models.IntegerField()
    Item_Name=models.CharField(max_length=250)
    Description=models.CharField(max_length=250)

    def __str__(self):
        return self.Item_Name
