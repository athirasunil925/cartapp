from django.contrib import admin
from . models import Category,Product
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
# class Category_admin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
# admin.site.register(Category,Category_admin)
#
# class Product_admin(admin.ModelAdmin):
#     list_display = ['name','price']
#     list_editable = ['price']
#     prepopulated_fields = {'slug':('name',)}
# admin.site.register(Product,Product_admin)