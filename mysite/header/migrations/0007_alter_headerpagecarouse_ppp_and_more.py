# Generated by Django 4.0.4 on 2022-05-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0006_alter_headerpagecarouse_ppp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerpagecarouse',
            name='ppp',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='headerpagecarouse',
            name='sub_title',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
