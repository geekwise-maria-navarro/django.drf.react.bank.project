from django.db import models

# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=200, default='Full name')
    branch_location = models.CharField(max_length=200)

    def __str__(self):
        return self.branch_name

class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return (f"Name: {self.customer_name} | Email: {self.customer_email} | Location: {self.branch.bank_name}")

class Product(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE
    )
    product_options = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('debit', 'DEBIT'),
        ('credit', 'CREDIT'),
    )
    product_options = models.CharField(
        max_length=200,
        choices = product_options,
        default = product_options[0]
    )
    def __str__(self):
            return (f"Customer Name: {self.customer.customer_name}")