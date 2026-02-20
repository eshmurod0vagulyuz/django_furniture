from django.db import models

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.id}|{self.title}"



class Products(models.Model):
    image = models.ImageField(upload_to='banner/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=64)
    info =models.CharField(max_length=255)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.id}|{self.title}"

