# Generated by Django 3.1.2 on 2020-11-27 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0004_auto_20201125_0702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='garbagenodes',
            options={'ordering': ['amount']},
        ),
    ]