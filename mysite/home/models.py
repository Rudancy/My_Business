from django.db import models

# Create your models here.

class home_page(models.Model):
    masthead = models.CharField(max_length=30, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    icon_1_header = models.CharField(max_length=30, default='', blank=True)
    icon_1_description = models.TextField(max_length=30, default='', blank=True)
    icon_2_header = models.CharField(max_length=30, default='', blank=True)
    icon_2_description = models.TextField(max_length=30, default='', blank=True)
    icon_3_header = models.CharField(max_length=30, default='', blank=True)
    icon_3_description = models.TextField(max_length=30, default='', blank=True)
    showcase_1_header = models.CharField(max_length=30, default='', blank=True)
    showcase_1_image = models.ImageField(upload_to='images', default='', blank=True)
    showcase_1_description = models.TextField(max_length=100, default='', blank=True)
    showcase_2_header = models.CharField(max_length=30, default='', blank=True)
    showcase_2_image = models.ImageField(upload_to='images', default='', blank=True)
    showcase_2_description = models.TextField(max_length=100, default='', blank=True)
    showcase_3_header = models.CharField(max_length=30, default='', blank=True)
    showcase_3_image = models.ImageField(upload_to='images', default='', blank=True)
    showcase_3_description = models.TextField(max_length=100, default='', blank=True)
    
    
    def __str__(self):
        return self.masthead
