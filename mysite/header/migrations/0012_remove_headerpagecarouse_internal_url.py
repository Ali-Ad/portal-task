# Generated by Django 4.0.4 on 2022-05-15 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0011_alter_headerpagecarouse_internal_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerpagecarouse',
            name='internal_url',
        ),
    ]
