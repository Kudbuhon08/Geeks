# Generated by Django 4.2.6 on 2023-10-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0003_settings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='image',
            field=models.ImageField(upload_to='geeks_image/', verbose_name='Фотография'),
        ),
    ]
