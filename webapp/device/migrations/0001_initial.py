# Generated by Django 3.2.8 on 2021-10-17 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('hard_disk', models.CharField(max_length=255)),
                ('CPU', models.CharField(max_length=255)),
                ('memory', models.CharField(max_length=255)),
            ],
        ),
    ]