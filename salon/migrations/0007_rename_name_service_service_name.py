# Generated by Django 4.2 on 2023-05-15 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0006_rename_time_required_service_required_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='service_name',
        ),
    ]
