# Generated by Django 3.2.3 on 2021-05-28 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0005_auto_20210528_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='total_price',
        ),
    ]
