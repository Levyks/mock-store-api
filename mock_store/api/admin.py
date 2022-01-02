from django.contrib import admin

from .models import Product, Category, User, Client, Order, OrderStatus, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]

class CategoryProductInline(admin.TabularInline):
    model = Product.categories.through
    verbose_name = "product"
    can_delete = False

    def has_add_permission(self, request, obj=None):
      return False

    def has_change_permission(self, request, obj=None):
      return False

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryProductInline]

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)