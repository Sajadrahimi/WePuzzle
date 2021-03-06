# Generated by Django 2.2.1 on 2019-05-11 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0002_auto_20190511_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='next_puzzle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_previous_puzzle', to='puzzle.puzzle'),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='previous_puzzle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_next_puzzle', to='puzzle.puzzle'),
        ),
    ]
