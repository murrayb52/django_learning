# Generated by Django 3.0 on 2021-03-13 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0003_auto_20210313_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcourses',
            name='startedfrom',
        ),
    ]
