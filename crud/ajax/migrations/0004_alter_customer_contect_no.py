# Generated by Django 3.2.3 on 2021-05-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0003_auto_20210528_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contect_no',
            field=models.IntegerField(blank=True),
        ),
    ]
