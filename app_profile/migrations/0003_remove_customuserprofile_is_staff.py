# Generated by Django 3.1.1 on 2020-09-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0002_customuserprofile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserprofile',
            name='is_staff',
        ),
    ]