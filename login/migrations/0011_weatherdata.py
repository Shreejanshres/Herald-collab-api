# Generated by Django 4.1.7 on 2023-04-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_user_farmer_dob_user_farmer_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='weatherdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('temperature', models.CharField(max_length=50)),
                ('humidity', models.CharField(max_length=50)),
                ('maxtemp', models.CharField(max_length=50)),
                ('mintemp', models.CharField(max_length=50)),
            ],
        ),
    ]
