# Generated by Django 5.0.1 on 2024-02-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_items_date_items_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.CharField(default='null description', max_length=10000),
            preserve_default=False,
        ),
    ]
