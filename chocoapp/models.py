from django.db import models

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_seasonal = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    suggested_flavor = models.CharField(max_length=100)
    allergy_concern = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.suggested_flavor}"

