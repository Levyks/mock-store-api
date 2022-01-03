from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .managers import UserProfileManager

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    can_change_password = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class Client(models.Model):
    
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    

class OrderStatus(models.Model):

    class Meta:
        verbose_name_plural = 'order status'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderProduct")
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=1)
    
    delivery_address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.client.user.first_name} {self.client.user.last_name}'

class OrderProduct(models.Model):

    class Meta:
        db_table = 'api_order_products'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
