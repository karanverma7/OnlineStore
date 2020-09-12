from django.db import models


class Product(models.Model):
    '''Model for managing products'''

    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    detail = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    '''Model for managing order placed'''

    name = models.CharField(max_length=120)
    address = models.TextField()
    city = models.CharField(max_length=100)
    items = models.CharField(max_length=200)
    orderStatus = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)

    def __str__(self):
        return self.name
