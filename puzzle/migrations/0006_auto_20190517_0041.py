# Generated by Django 2.2.1 on 2019-05-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0005_auto_20190513_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='puzzle_hinted_page',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='puzzle_hinted_password',
            field=models.TextField(blank=True, null=True),
        ),
    ]