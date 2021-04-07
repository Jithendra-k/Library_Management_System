from django.db import models

# Create your models here.


class OOPS(models.Model):
    o_id=models.AutoField(primary_key=True)
    o_name=models.CharField(max_length=100)
    o_year=models.IntegerField(max_length=5)