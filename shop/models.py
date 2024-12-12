from django.db import models
from .managers import CategoryManager,ItemManager,TagManager

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    objects=CategoryManager()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    objects=ItemManager()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tags', blank=True)
    objects=TagManager()
    def __str__(self):
        return self.name