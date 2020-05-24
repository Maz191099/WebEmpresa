from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('name', 'key', ) 
    list_display = ('name', 'url', ) 

admin.site.register(Link, LinkAdmin)
