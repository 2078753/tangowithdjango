from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

admin.site.register(UserProfile)

class Display(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
