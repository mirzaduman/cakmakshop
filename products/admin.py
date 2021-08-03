from django.contrib import admin
from . import models


class CakmakAdmin(admin.ModelAdmin):
    list_display = ('marka', 'model', 'no', 'fiyat')
    list_per_page = 24
    search_fields = ('marka', 'model', 'no')


admin.site.register(models.Cakmak, CakmakAdmin)
admin.site.register(models.Marka)
