# Generated by Django 4.1.7 on 2023-05-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0004_rename_address_booking_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='PEOPLE',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
