# Generated by Django 3.2.4 on 2021-06-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0008_alter_customer_phone2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='document',
            field=models.PositiveIntegerField(),
        ),
    ]
