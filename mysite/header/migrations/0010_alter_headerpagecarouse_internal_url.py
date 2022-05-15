# Generated by Django 4.0.4 on 2022-05-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('header', '0009_alter_headerpagecarouse_internal_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerpagecarouse',
            name='internal_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
