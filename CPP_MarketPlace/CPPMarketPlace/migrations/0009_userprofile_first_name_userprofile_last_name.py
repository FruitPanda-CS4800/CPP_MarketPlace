# Generated by Django 4.1.7 on 2023-05-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPPMarketPlace', '0008_userprofile_about_userprofile_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='default', max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='default', max_length=30),
        ),
    ]