# Generated by Django 4.2.6 on 2023-10-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0002_alter_settings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='image',
            field=models.ImageField(default=1, upload_to=True, verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
