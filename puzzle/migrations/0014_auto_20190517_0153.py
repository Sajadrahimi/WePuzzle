# Generated by Django 2.2.1 on 2019-05-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0013_auto_20190517_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wrong_page',
            name='wrong_page_title',
            field=models.CharField(blank=True, default='Wrong', max_length=30),
        ),
    ]
