# Generated by Django 4.1.7 on 2023-03-29 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_crops_detail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='crops_detail',
        ),
        migrations.DeleteModel(
            name='Farmer',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
