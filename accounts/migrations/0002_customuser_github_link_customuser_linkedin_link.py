# Generated by Django 4.0.6 on 2024-06-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='github_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
