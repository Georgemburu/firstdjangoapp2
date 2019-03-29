from django.db import models
# other
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price  = models.DecimalField(max_digits=1000, decimal_places=2)
    active = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("product:give_product_id", kwargs={ "id": self.id})
        # return f"/product/{self.id}"
        
