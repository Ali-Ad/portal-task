# Generated by Django 4.0.4 on 2022-05-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0005_headerpagecarouse_ppp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerpagecarouse',
            name='ppp',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='headerpagecarouse',
            name='sub_title',
            field=models.CharField(max_length=2),
        ),
    ]
