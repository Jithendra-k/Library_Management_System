from django.db import models

# Create your models here.


class Maths(models.Model):
    m_id=models.AutoField(primary_key=True)
    m_name=models.CharField(max_length=100)
    m_year=models.IntegerField(max_length=5)