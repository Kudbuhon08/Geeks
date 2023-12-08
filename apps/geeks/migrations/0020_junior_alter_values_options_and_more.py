# Generated by Django 5.0 on 2023-12-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0019_alter_values_options_values_descriptions4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Junior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('title1', models.CharField(max_length=50, verbose_name='Заголовок 1')),
                ('descriptions1', models.CharField(max_length=500, verbose_name='Описание 1')),
                ('title2', models.CharField(max_length=50, verbose_name='Заголовок 2')),
                ('descriptions2', models.CharField(max_length=500, verbose_name='Описание 2')),
                ('title3', models.CharField(max_length=50, verbose_name='Заголовок 3')),
                ('descriptions3', models.CharField(max_length=500, verbose_name='Описание 3')),
                ('title4', models.CharField(max_length=50, verbose_name='Заголовок 4')),
                ('descriptions4', models.CharField(max_length=500, verbose_name='Описание 4')),
            ],
            options={
                'verbose_name': ('Junior',),
                'verbose_name_plural': 'JUnior',
            },
        ),
        migrations.AlterModelOptions(
            name='values',
            options={'verbose_name': ('Ценность',), 'verbose_name_plural': 'Ценности'},
        ),
        migrations.RemoveField(
            model_name='values',
            name='descriptions4',
        ),
        migrations.RemoveField(
            model_name='values',
            name='title4',
        ),
    ]
