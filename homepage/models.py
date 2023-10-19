from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import Group  




class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Add a related_name argument to avoid clashes
    groups = models.ManyToManyField(Group, verbose_name='Groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='User Permissions', blank=True, related_name='custom_user_permissions')

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    # Define the category field as a CharField with choices
    CATEGORY_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Role-Playing', 'Role-Playing'),
        ('Simulation', 'Simulation'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Puzzle', 'Puzzle'),
        ('Other', 'Other'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Other',
    )

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='purchases')
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Purchase by {self.user.username} on {self.purchase_date}'
    
    
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='BasketItem')

    def total_price(self):
        # Calculate the total price of items in the shopping basket
        total = 0
        for item in self.basketitem_set.all():
            total += item.product.price * item.quantity
        return total

class BasketItem(models.Model):
    basket = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()