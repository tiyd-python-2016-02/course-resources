from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=140)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=140)
    products = models.ManyToManyField(Product)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    user = models.OneToOneField(User, null=True)

    def get_total(self):
        total = 0
        for product in self.products.all():
            total += product.price
        return total
