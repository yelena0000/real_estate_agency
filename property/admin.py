from django.contrib import admin
from .models import (
    Complaint,
    Flat,
    Owner,
    Ownership
)


class OwnershipInline(admin.TabularInline):
    model = Ownership
    extra = 2
    raw_id_fields = ('owner', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone_number',
        'normalized_phone',
        'display_owned_flats'
    )
    search_fields = (
        'full_name',
        'phone_number'
    )
    inlines = [OwnershipInline]

    def display_owned_flats(self, obj):
        return ", ".join(flat.address for flat in obj.ownerships.all())

    display_owned_flats.short_description = "Квартиры в собственности"


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'town',
        'address',
        'ownerships__owner__full_name',
    )
    readonly_fields = (
        'created_at',
    )
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'active',
    )
    list_editable = (
        'new_building',
    )
    list_filter = (
        'new_building',
        'active',
        'has_balcony',
        'rooms_number',
    )
    raw_id_fields = (
        'liked_by',
    )
    inlines = [OwnershipInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'flat',
        'text'
    )
    search_fields = (
        'user__username',
        'flat__address'
    )
    raw_id_fields = (
        'user',
        'flat'
    )