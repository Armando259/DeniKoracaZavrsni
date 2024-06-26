# Generated by Django 3.2.22 on 2024-06-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_vehicle_price_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black'), ('white', 'White'), ('silver', 'Silver'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('brown', 'Brown')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(choices=[('toyota', 'Toyota'), ('ford', 'Ford'), ('bmw', 'BMW'), ('audi', 'Audi'), ('mercedes', 'Mercedes-Benz'), ('honda', 'Honda'), ('chevrolet', 'Chevrolet'), ('nissan', 'Nissan'), ('volkswagen', 'Volkswagen'), ('hyundai', 'Hyundai')], max_length=20),
        ),
    ]
