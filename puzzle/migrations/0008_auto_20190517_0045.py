# Generated by Django 2.2.1 on 2019-05-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0007_auto_20190517_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puzzle',
            name='puzzle_hinted_page',
        ),
        migrations.AddField(
            model_name='hint_password',
            name='hinted_page',
            field=models.CharField(max_length=30, null=True),
        ),
    ]