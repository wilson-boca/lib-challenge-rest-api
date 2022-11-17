from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=13)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    commission = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)

    def __str__(self):
        return self.description


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Sell(models.Model):
    fiscal_code = models.CharField(max_length=8)
    date = models.DateTimeField()
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="client")
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE, related_name="seller")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)


class DayRule(models.Model):
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    min = models.IntegerField()
    max = models.IntegerField()

    def __str__(self):
        return DAYS_OF_WEEK[int(self.days)][1]

