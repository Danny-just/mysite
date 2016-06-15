from django.db import models

# Create your models here.
from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=200)
    signup_date = models.DateTimeField('date published')


