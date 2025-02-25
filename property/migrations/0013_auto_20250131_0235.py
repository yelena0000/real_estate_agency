# Generated by Django 2.2.24 on 2025-01-30 23:35

from django.db import migrations


def link_owners_with_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owners = Owner.objects.filter(
            full_name=flat.owner,
            phone_number=flat.owners_phonenumber,
            normalized_phone=flat.owner_pure_phone
        )
        flat.owners.set(owners)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20250131_0217'),
    ]

    operations = [
        migrations.RunPython(link_owners_with_flats),
    ]
