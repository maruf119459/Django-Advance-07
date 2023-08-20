from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # 120.34
    def __str__(self):
        return self.name

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    review = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True) # obj jokhon toiri hoyche tokhon kar time save kore rakhbe
    updated_at = models.DateTimeField(auto_now=True) #user jokhon review editr korbe tokhon kar time save kore rakhbe
    class Meta:
        unique_together = ('product', 'user') # ekta product er biporite ekjon user ekta comment korte parbe. unique_together default variable
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name} - Rating: {self.rating}"