from django.contrib import admin
from .models import Account, Country, Region, District, VerifyPhone
from modeltranslation.admin import TranslationAdmin


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    pass


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    pass


@admin.register(District)
class DistrictAdmin(TranslationAdmin):
    pass


@admin.register(VerifyPhone)
class VerifyPhoneAdmin(admin.ModelAdmin):
    pass
