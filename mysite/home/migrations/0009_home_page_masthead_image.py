# Generated by Django 3.1.7 on 2021-06-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210601_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_page',
            name='masthead_image',
            field=models.ImageField(blank=True, default='', upload_to='static/images'),
        ),
    ]
