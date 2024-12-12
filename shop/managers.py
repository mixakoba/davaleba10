from django.db import models
from django.db.models import Count

class CategoryManager(models.Model):
    def with_item_count(self):
        return self.get_queryset().annotate(item_count=Count('items'))    
    
class ItemManager(models.Manager):
    def with_tag_count(self):
        return self.get_queryset().annotate(tags_count=Count('tags'))
    
class TagManager(models.Manager):
    def popular_tags(self, min_items):
        return self.get_queryset().annotate(item_count=Count('items')).filter(item_count__gte=min_items)