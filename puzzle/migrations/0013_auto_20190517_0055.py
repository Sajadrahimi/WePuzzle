# Generated by Django 2.2.1 on 2019-05-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0012_remove_wrong_page_wrong_page_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint_password',
            name='hinted_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='puzzle.wrong_page'),
        ),
    ]
