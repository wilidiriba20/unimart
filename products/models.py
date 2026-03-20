from django.db import models
from django.conf import settings   # ✅ ADD THIS

class Product(models.Model):

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('like new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('used', 'Used'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ correct now

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title