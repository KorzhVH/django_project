# Generated by Django 4.2 on 2023-05-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0003_alter_master_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='rank',
            field=models.IntegerField(choices=[(1, 'Junior'), (2, 'Senior')], default=1),
        ),
    ]
