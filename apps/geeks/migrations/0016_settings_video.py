# Generated by Django 5.0 on 2023-12-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0015_alter_about_title_alter_settings_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='video',
            field=models.URLField(default=1, verbose_name='видео'),
            preserve_default=False,
        ),
    ]
