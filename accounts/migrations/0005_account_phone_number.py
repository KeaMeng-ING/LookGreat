# Generated by Django 3.1 on 2024-03-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20240131_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
