# Generated by Django 4.2 on 2023-05-09 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='master_id',
            new_name='master',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='master_id',
            new_name='master',
        ),
    ]
