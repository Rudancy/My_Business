# Generated by Django 3.1.7 on 2021-08-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_home_page_masthead_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_page',
            name='showcase_1_description',
            field=models.TextField(blank=True, default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='home_page',
            name='showcase_2_description',
            field=models.TextField(blank=True, default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='home_page',
            name='showcase_3_description',
            field=models.TextField(blank=True, default='', max_length=600),
        ),
    ]
