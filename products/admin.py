from django.contrib import admin
from .models import Product, IndicatorDownload, Lead

# Register your models here.
admin.site.register(IndicatorDownload)
admin.site.register(Lead)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_free')