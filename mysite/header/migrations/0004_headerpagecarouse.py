# Generated by Django 4.0.4 on 2022-05-15 13:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0003_remove_headerpage_sub_title_alter_headerpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderPageCarouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('sub_title', models.CharField(max_length=50)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousal_Header', to='header.headerpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
