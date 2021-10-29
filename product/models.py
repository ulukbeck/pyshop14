from django.db import models
from django.db.models.deletion import CASCADE

# TODO: Create category 'Samsung(smartphone)'
# TODO: CReate parent category: laptops - -> Acer, Macbook, Asus
# TODO: Accessories - -> Earphones, Powerbanks, 
# TODO: for each category create 2 products 
# charfield = varchar

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    
    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title
    
class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'In stock'),
        ('out of stock', 'Out of stock'),
        ('awaiting', 'Awaiting')
    )
    name = models.CharField(max_length=155)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='prod_images')
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name

    
    
    