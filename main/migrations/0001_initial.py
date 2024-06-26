# Generated by Django 3.2.22 on 2024-06-05 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('toyota', 'Toyota'), ('ford', 'Ford'), ('bmw', 'BMW')], max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('license_plate', models.CharField(max_length=10)),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
                ('is_available', models.BooleanField(default=True)),
                ('price_per_day', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('category', models.CharField(choices=[('mali', 'Mali'), ('srednji', 'Srednji'), ('veliki', 'Veliki'), ('kombi', 'Kombi')], default='mali', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_korisnika', models.CharField(max_length=100)),
                ('prezime_korisnika', models.CharField(max_length=100)),
                ('adresa_korisnika', models.CharField(max_length=100)),
                ('mobitel_korisnika', models.CharField(max_length=10)),
                ('email_korisnika', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
