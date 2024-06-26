# Generated by Django 5.0.6 on 2024-06-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0003_alter_city_options_alter_city_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb4_general_ci', max_length=1000, null=True)),
                ('account_number', models.CharField(blank=True, db_collation='utf8mb4_general_ci', max_length=1000, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Customer',
                'db_table': 'Customer',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'managed': False, 'verbose_name_plural': 'atm_city'},
        ),
        migrations.AlterModelTable(
            name='city',
            table='atm_city',
        ),
    ]
