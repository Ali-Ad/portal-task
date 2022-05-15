# Generated by Django 4.0.4 on 2022-05-14 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Footer Page',
                'verbose_name_plural': 'Footer Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
