# Generated by Django 4.1.5 on 2023-01-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formMail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineerstudents',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='medicalstudents',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
