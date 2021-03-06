from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=64, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
