from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255)
    population = models.PositiveIntegerField()
    land_area = models.PositiveIntegerField()
    flag = models.ImageField(null=True, upload_to='flags/')

    @property
    def is_transcontinental(self):
        return len(self.continents.all()) > 1

    @property
    def has_multiple_capital_cities(self):
        return len(self.capital_city.all()) > 1

    def __str__(self):
        return self.name


class Continent(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField()
    land_area = models.PositiveIntegerField(null=True)
    countries = models.ManyToManyField(Country, related_name='continents')

    @property
    def country_count(self):
        return len(self.countries.all())

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    population = models.PositiveIntegerField()
    is_country_capital = models.BooleanField(default=False)
    special_note = models.CharField(max_length=100, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='capital_city')

    def __str__(self):
        if self.is_country_capital and self.special_note is not '':
            return f"{self.name} ({self.special_note})"
        else:
            return self.name
