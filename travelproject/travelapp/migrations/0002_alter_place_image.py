# Generated by Django 4.0.5 on 2022-06-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
