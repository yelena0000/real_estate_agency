# Generated by Django 2.2.24 on 2025-01-30 22:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250131_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('normalized_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='flats', to='property.Owner', verbose_name='Собственники квартиры'),
        ),
    ]
