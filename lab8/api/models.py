from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 500)



    def __str__(self):
        return self.name
    
    def to_json(self):
        return {
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length = 500)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    

    def __str__(self):
        return self.name
    
    def to_json(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
        }