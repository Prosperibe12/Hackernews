# Generated by Django 4.1.1 on 2022-09-22 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hnapp', '0003_stories_kids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stories',
            name='kids',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='text',
        ),
    ]
