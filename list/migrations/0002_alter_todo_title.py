# Generated by Django 4.0.6 on 2022-08-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
