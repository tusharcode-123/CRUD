# Generated by Django 3.2.3 on 2021-05-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrudUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]