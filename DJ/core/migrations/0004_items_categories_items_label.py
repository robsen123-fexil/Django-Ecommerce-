# Generated by Django 5.0.1 on 2024-01-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_item_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='categories',
            field=models.CharField(choices=[('S', 'shirts'), ('SW', 'sportshirt'), ('OW', 'outwear')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='label',
            field=models.CharField(choices=[('p', 'primary'), ('s', 'secondary'), ('d', 'danger')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
