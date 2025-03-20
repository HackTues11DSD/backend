# Generated by Django 5.1.7 on 2025-03-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('symptoms', models.TextField()),
                ('recommendations', models.TextField()),
            ],
        ),
    ]
