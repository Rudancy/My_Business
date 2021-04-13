from django.db import models

# Create your models here.

class home_page(models.Model):
    masthead = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=200, default='')
    icon_1_header = models.CharField(max_length=30, default='')
    icon_1_description = models.TextField(max_length=30, default='')
    icon_2_header = models.CharField(max_length=30, default='')
    icon_2_description = models.TextField(max_length=30, default='')
    icon_3_header = models.CharField(max_length=30, default='')
    icon_3_description = models.TextField(max_length=30, default='')
    showcase_1_header = models.CharField(max_length=30, default='')
    showcase_1_image = models.ImageField(upload_to='images', default='')
    showcase_1_description = models.TextField(max_length=100, default='')
    showcase_2_header = models.CharField(max_length=30, default='')
    showcase_2_image = models.ImageField(upload_to='images', default='')
    showcase_2_description = models.TextField(max_length=100, default='')
    showcase_3_header = models.CharField(max_length=30, default='')
    showcase_3_image = models.ImageField(upload_to='images', default='')
    showcase_3_description = models.TextField(max_length=100, default='')
    
    
    def __str__(self):
        return self.masthead, self.description, self.icon_1_header, self.icon_1_description, self.icon_2_header, self.icon_2_description, 
        self.icon_3_header, self.icon_3_description, self.showcase_1_header, self.showcase_1_image, self.showcase_1_description, self.showcase_2_header, 
        self.showcase_2_image, self.showcase_2_description, self.showcase_3_header, self.showcase_3_image, self.showcase_3_description 
