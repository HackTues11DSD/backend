# Generated by Django 5.1.6 on 2025-03-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_api', '0003_remove_cause_symptoms_remove_symptom_key_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injury',
            name='recommendations',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='symptoms',
        ),
         migrations.RemoveField(
            model_name='injury',
            name='place',
        ),
    ]
