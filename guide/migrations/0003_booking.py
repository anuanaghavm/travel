# Generated by Django 4.1.7 on 2023-05-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_login_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('EMAIL', models.CharField(max_length=50)),
                ('PHONENUMBER', models.IntegerField()),
                ('ADDRESS', models.CharField(max_length=200)),
            ],
        ),
    ]