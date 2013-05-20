from django.contrib import admin
from pages.models import HomePage, Category

class HomePageAdmin(admin.ModelAdmin):
	list_display = ['title','date','thumbnail','category_']
	list_filter  = ['date','category']
	
class CategoryAdmin(admin.ModelAdmin):
	search_fields =['tag']
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Category, CategoryAdmin)
