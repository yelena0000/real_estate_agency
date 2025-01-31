from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 2
    raw_id_fields = ('owner',)


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
    raw_id_fields = (
        'flats',
    )

    def display_owned_flats(self, obj):
        return obj.owned_flats()

    display_owned_flats.short_description = "Квартиры в собственности"


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'town',
        'address',
        'owners__full_name',
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
        'owners'
    )
    inlines = [OwnerInline]


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
