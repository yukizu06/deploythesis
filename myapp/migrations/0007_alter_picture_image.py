# Generated by Django 4.1.3 on 2023-01-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_picture_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='images\\medicaldata'),
        ),
    ]
