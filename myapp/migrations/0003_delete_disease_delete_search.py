# Generated by Django 4.1.3 on 2023-01-15 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230105_1106'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
