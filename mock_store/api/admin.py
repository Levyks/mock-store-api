from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

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

class CustomUserAdmin(UserAdmin):    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Client)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)