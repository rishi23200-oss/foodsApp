from django.db import models

# Create your models here.

class FoodItems(models.Model):
    Catageries = [
        ("PIZZA","Pizza"),
        ("BURGER","Burger"),
        ("FRENCH FRIES","French Fries"),
        ("DESSARTS","Dessarts"),
        ("BREVERAGES","Breverages"),
        ("BRIYANI","Briyani")
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    foodimg = models.ImageField(upload_to = "foodimg/",blank=True,null = True)
    description = models.TextField()
    catogery = models.CharField(max_length=100,choices=Catageries)
    
    def __str__(self):
        return self.name