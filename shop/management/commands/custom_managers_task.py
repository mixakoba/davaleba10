from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        categories=Category.objects.with_item_count()
        print("Categories with item count:")
        for category in categories:
            print(f"{category.name}: {category.item_count} items")
        
        items = Item.objects.with_tag_count()
        print("Items with tag count:")
        for item in items:
            print(f"{item.name}: {item.tags_count} tags")
        
        min_items=5
        popular_tags = Tag.objects.popular_tags(min_items)
        print(f"Popular tags with at least {min_items} items:")
        for tag in popular_tags:
            print(f"{tag.name}: {tag.item_count} items")