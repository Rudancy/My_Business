from django.db import models

# Create your models here.

class business_site_header(models.Model):
    title = models.CharField(max_length=30)
    descrition = models.TextField(max_length=200)
