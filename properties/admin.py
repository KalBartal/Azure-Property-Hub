from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at')

admin.site.register(Property, PropertyAdmin)
