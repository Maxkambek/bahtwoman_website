from .models import District, Region, Country
from modeltranslation.translator import TranslationOptions, register


@register(Country)
class CountryTrans(TranslationOptions):
    fields = ('name',)


@register(Region)
class RegionTrans(TranslationOptions):
    fields = ('name',)


@register(District)
class DistrictTrans(TranslationOptions):
    fields = ('name',)
