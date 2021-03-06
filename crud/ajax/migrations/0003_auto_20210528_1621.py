# Generated by Django 3.2.3 on 2021-05-28 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0002_auto_20210527_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('contect_no', models.IntegerField(blank=True, max_length=100)),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.IntegerField(default=1)),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajax.customer')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='CrudUser',
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajax.product'),
        ),
    ]
