# Generated by Django 5.0.1 on 2024-02-01 11:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_items_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
