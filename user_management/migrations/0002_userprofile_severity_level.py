# Generated by Django 5.1.6 on 2025-02-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='severity_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
