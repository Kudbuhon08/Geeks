# Generated by Django 5.0 on 2023-12-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0018_alter_values_descriptions1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='values',
            options={'verbose_name': ('Junior',), 'verbose_name_plural': 'JUnior'},
        ),
        migrations.AddField(
            model_name='values',
            name='descriptions4',
            field=models.CharField(default=1, max_length=500, verbose_name='Описание 4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='values',
            name='title4',
            field=models.CharField(default=1, max_length=50, verbose_name='Заголовок 4'),
            preserve_default=False,
        ),
    ]
