# Generated by Django 3.1.1 on 2020-09-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0004_auto_20200918_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserprofile',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
