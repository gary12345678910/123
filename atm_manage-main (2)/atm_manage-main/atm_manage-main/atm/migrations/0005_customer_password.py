# Generated by Django 5.0.6 on 2024-06-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0004_customer_alter_city_options_alter_city_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, db_collation='utf8mb4_general_ci', max_length=1000, null=True),
        ),
    ]
