from django.contrib import admin
from .models import Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title', 'content', ) 
    list_display = ('title',  )

admin.site.register(Page, PageAdmin)