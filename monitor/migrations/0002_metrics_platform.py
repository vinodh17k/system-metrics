# Generated by Django 2.2.7 on 2019-12-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrics',
            name='platform',
            field=models.TextField(default=''),
        ),
    ]