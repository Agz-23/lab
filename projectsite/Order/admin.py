from django.contrib import admin
from Order.models import Brand, Comment, Customer, Order, Shoe

# class BaseModelAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at', 'updated_at')

# class BrandAdmin(BaseModelAdmin):
#     list_display = ('name', 'display_created_at', 'display_updated_at')

# class CommentAdmin(BaseModelAdmin):
#     list_display = ('author', 'product', 'text', 'rating', 'display_created_at', 'display_updated_at')

# class CustomerAdmin(BaseModelAdmin):
#     list_display = ('name', 'location', 'email', 'display_created_at', 'display_updated_at')

# class OrderAdmin(BaseModelAdmin):
#     list_display = ('customer', 'date_ordered', 'total_amount', 'display_created_at', 'display_updated_at')

# class ShoeAdmin(BaseModelAdmin):
#     list_display = ('brand', 'name', 'color', 'size', 'price', 'display_created_at', 'display_updated_at')

admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Shoe)
