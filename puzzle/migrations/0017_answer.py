# Generated by Django 2.2.1 on 2019-05-25 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190517_0138'),
        ('puzzle', '0016_auto_20190524_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.TextField()),
                ('answer_created_time', models.DateField()),
                ('answer_created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.User')),
            ],
        ),
    ]
