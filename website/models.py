from django.db import models

# Create your models here.

# Test
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name
# End Test