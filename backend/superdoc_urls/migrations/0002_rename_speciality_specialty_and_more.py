# Generated by Django 5.1.6 on 2025-03-21 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superdoc_urls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Speciality',
            new_name='Specialty',
        ),
        migrations.RenameField(
            model_name='specialty',
            old_name='specalty_id',
            new_name='specialty_id',
        ),
    ]
