# Generated by Django 5.0 on 2023-12-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0014_remove_settings_image_2_about_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
