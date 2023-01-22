from django.contrib import admin
from .models import Product, Category, Seller, Rating, Callback, Order, Basket
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Product)
class products(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Category)
class categories(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
        
@admin.register(Seller)
class sallers(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Rating)
class ratings(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Callback)
class callbacks(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
        
@admin.register(Order)
class orders(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Basket)
class baskets(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True