# Generated by Django 2.2.1 on 2019-05-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0020_remove_puzzle_puzzle_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='puzzle_audio',
            field=models.FileField(blank=True, null=True, upload_to='puzzle_audios'),
        ),
    ]