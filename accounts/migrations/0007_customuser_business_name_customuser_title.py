# Generated by Django 5.2 on 2025-05-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_subscription_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='business_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
