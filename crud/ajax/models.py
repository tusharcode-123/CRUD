from django.db import models

# Create your models here.
class customer(models.Model):
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    contect_no = models.CharField(max_length=10,blank=True)
    pincode = models.IntegerField()

    def __str__(self):
        return self.first_name

class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class order(models.Model):
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        qu = self.quantity
        pr = self.price
        total = qu * pr
        return total
