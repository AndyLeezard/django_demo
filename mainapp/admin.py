from django.contrib import admin

from .models import Country, Item, Location, Visitor

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('location',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Country)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location)
admin.site.register(Visitor)