# Generated by Django 5.0.1 on 2024-01-30 17:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_items_categories_items_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
        ),
    ]