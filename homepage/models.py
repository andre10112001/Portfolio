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
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

