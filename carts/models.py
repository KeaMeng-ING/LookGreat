from django.db import models

from store.models import Product, Variation
from accounts.models import Account

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True) # blank=True means that the field is not required
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True) # null=True means that the field is not required
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation, blank=True) # Many to Many relationship with Variation model
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self): # __unicode__ is used to return the string representation of the object
        return self.product