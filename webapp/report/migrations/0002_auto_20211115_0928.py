# Generated by Django 3.2.8 on 2021-11-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='deposit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='serviceCost',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='total',
            field=models.CharField(max_length=200, null=True),
        ),
    ]