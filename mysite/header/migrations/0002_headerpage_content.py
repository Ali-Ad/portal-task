# Generated by Django 4.0.4 on 2022-05-15 12:32

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Header', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('page', wagtail.core.blocks.PageChooserBlock(max_length=40, required=False)), ('page_url', wagtail.core.blocks.URLBlock(max_length=60, required=False))])))]))], blank=True, null=True),
        ),
    ]
