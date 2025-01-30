from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = [
        'town',
        'address',
        'owner'
    ]
    readonly_fields = [
        'created_at'
    ]
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = [
        'new_building',
    ]
    list_filter = [
        'new_building',
        'active',
        'has_balcony',
        'rooms_number',
        'town',
    ]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'flat',
        'text'
    ]
    raw_id_fields = [
        'user',
        'flat'
    ]
