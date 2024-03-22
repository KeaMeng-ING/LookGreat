from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} # This will automatically create a slug based on the category name
    list_display = ('category_name', 'slug') # This will display the category name and slug in the admin panel


admin.site.register(Category, CategoryAdmin)