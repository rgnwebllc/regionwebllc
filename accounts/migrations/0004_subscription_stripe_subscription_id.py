# Generated by Django 5.2 on 2025-05-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
