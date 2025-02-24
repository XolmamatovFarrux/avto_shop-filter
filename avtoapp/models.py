from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'car'
        verbose_name = 'Car_brand'
        verbose_name_plural = 'Car_brands'
        ordering = ['brand']

    def __str__(self):
        return self.brand


class Car_s(models.Model):
    title = models.CharField(max_length=100)
    brand = models.ForeignKey(Car, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    context = models.TextField(blank=True)
    horsepower =models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cars'
        verbose_name = 'cara'
        verbose_name_plural = 'cars'
        ordering = ['year']

    def __str__(self):
        return self.title