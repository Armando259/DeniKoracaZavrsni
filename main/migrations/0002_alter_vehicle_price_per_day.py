# Generated by Django 3.2.22 on 2024-06-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='price_per_day',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
        ),
    ]
