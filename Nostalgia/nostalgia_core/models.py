from django.db import models

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=200)

    