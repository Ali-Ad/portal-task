# Generated by Django 4.0.4 on 2022-05-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0004_headerpagecarouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerpagecarouse',
            name='ppp',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
