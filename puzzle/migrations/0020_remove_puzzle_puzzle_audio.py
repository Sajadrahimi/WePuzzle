# Generated by Django 2.2.1 on 2019-05-25 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0019_auto_20190525_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puzzle',
            name='puzzle_audio',
        ),
    ]
