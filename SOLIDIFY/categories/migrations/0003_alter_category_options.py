# Generated by Django 5.2.3 on 2025-07-04 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_category_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
