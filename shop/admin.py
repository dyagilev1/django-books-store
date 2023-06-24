from django.contrib import admin
from .models import Category, Product, Brand, Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}



class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryInline]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand', 'slug',)
    prepopulated_fields = {'slug': ('brand',)}

