from django.db import models
from django.contrib.auth.models import User

# Medieval RPG Store Types
STORE_TYPES = [
    ('general_store', 'General Store'),
    ('market_stall', 'Market Stall'),
    ('blacksmith', 'Blacksmith'),
    ('alchemist', 'Alchemist'),
    ('magic_shop', 'Magic Shop'),
    ('herbalist', 'Herbalist'),
    ('tailor', 'Tailor'),
    ('inn', 'Inn'),
    ('tavern', 'Tavern'),
    ('stable', 'Stable'),
    ('fletcher', 'Fletcher'),
]

# Medieval RPG Product Types
PRODUCT_TYPES = [
    ('weapon_melee', 'Melee Weapon'),
    ('weapon_ranged', 'Ranged Weapon'),
    ('shield', 'Shield'),
    ('armor_light', 'Light Armor'),
    ('armor_heavy', 'Heavy Armor'),
    ('potion_health', 'Health Potion'),
    ('potion_mana', 'Mana Potion'),
    ('scroll', 'Magic Scroll'),
    ('enchanted_item', 'Enchanted Item'),
    ('food', 'Food'),
    ('drink', 'Drink'),
    ('herb', 'Herb'),
    ('tool', 'Tool'),
    ('mount', 'Mount'),
]

class Store(models.Model):
    """Medieval RPG store model."""
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description_en = models.TextField(blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    store_type = models.CharField(max_length=20, choices=STORE_TYPES)

    def __str__(self):
        return f"{self.name} ({self.get_store_type_display()}) - {self.owner.username}"


class Product(models.Model):
    """Products with medieval RPG types."""
    name_en = models.CharField(max_length=255)
    name_es = models.CharField(max_length=255)
    description_en = models.TextField(blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)  # Product type

    def __str__(self):
        visibility = "Public" if self.is_public else "Private"
        return f"{self.name_en} ({self.get_product_type_display()} - {visibility})"


class StoreProduct(models.Model):
    """Relationship between stores and products."""
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("store", "product")

    def __str__(self):
        return f"{self.store.name} sells {self.product.name_en}"
