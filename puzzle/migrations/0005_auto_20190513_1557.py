# Generated by Django 2.2.1 on 2019-05-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0004_auto_20190513_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='puzzle_url',
            field=models.CharField(default='127.0.0.1', max_length=50),
        ),
    ]