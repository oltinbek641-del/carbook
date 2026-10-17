
from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nomi')
    brand = models.CharField(max_length=100, verbose_name='Markasi')
    model = models.CharField(max_length=100, verbose_name='Modeli')
    image = models.ImageField(upload_to='images/', verbose_name='Rasmi')
    description = models.TextField(verbose_name='Tavsifi')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Narxi')
    year = models.IntegerField(verbose_name='Ishlab chiqarilgan yili')
    color = models.CharField(max_length=50, verbose_name='Rangi')
    mileage = models.PositiveIntegerField(verbose_name='Yurgan masofasi')
    fuel_type = models.CharField(max_length=50, verbose_name='Yoqilg‘i turi')

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'

    def __str__(self):
        return self.title



