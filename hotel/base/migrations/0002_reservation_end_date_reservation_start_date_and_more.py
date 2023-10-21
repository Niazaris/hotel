# Generated by Django 4.2.6 on 2023-10-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
