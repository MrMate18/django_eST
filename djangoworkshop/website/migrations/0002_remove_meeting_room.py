# Generated by Django 5.0.1 on 2024-01-20 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='room',
        ),
    ]