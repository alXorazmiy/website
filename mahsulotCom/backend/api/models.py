from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    image = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.title 
    

class Category(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title 


class Product(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    amount = models.IntegerField(default = 0)
    price = models.FloatField(default = 0)
    image = models.TextField()
    active = models.BooleanField(default = True)
    shop = models.ForeignKey(Shop, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


    def __str__(self) -> str:
        return self.title 



class Image(models.Model):
    image = models.ImageField(upload_to='images/')