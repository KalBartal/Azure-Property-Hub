from django.db import models


class Property(models.Model):
    PROPERTY_TYPES = (
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
    )

    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='properties/photos', null=True, blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=8, decimal_places=2)
    year_built = models.IntegerField()
    garage_size = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.name
