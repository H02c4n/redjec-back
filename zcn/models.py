from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name_plural = 'Categories'



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.product_name} -- {self.quantity} '

    