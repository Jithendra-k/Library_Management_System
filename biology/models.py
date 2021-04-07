from django.db import models

# Create your models here.

class Biology(models.Model):
    b_id=models.AutoField(primary_key=True)
    b_name=models.CharField(max_length=100)
    b_year=models.IntegerField(max_length=5)