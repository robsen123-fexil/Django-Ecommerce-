# Generated by Django 5.0.1 on 2024-02-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_items_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='label',
        ),
        migrations.AlterField(
            model_name='items',
            name='categories',
            field=models.CharField(choices=[('T', 'shirts'), ('E', 'Electronics'), ('SW', 'SportWear')], max_length=2),
        ),
    ]
