# Generated by Django 3.2.4 on 2021-06-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=255)),
                ('specializedField', models.CharField(max_length=255)),
            ],
        ),
    ]
