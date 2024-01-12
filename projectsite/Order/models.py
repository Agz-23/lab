from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Shoe(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.brand} - {self.name} - {self.color} - Size {self.size} - ${self.price}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Order(BaseModel):
    date_ordered = models.DateField()
    products = models.ManyToManyField(Shoe)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"
    
class Comment(BaseModel):
    product = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(null=True, default=0)

    def __str__(self):
        return f'{self.author} - {self.product}'
    