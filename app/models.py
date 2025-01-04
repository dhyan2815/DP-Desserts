from django.db import models

class MenuItem(models.Model): 
    name = models.CharField(max_length=100) 
    description = models.TextField(max_length=200) 
    image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self): 
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(MenuItem)  # Many-to-Many Relationship
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    message = models.TextField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return f"Order #{self.id} by {self.name}"