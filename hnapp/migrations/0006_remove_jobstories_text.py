# Generated by Django 4.1.1 on 2022-09-23 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hnapp', '0005_askstories_jobstories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobstories',
            name='text',
        ),
    ]
