# Generated by Django 2.2.1 on 2019-05-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0014_auto_20190517_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='puzzle_hinted_password',
            field=models.ManyToManyField(blank=True, to='puzzle.hint_password'),
        ),
    ]
