from django.utils import timezone

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
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="client")
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE, related_name="seller")
    product = models.ManyToManyField(
        Product,
        through='Item'
    )

    def __str__(self):
        return str(self.id).zfill(8)

    @property
    def invoice(self):
        return str(self.id).zfill(8)

    @property
    def client_name(self):
        return self.client.name

    @property
    def seller_name(self):
        return self.seller.name

    @property
    def date_fmt(self):
        print(self.date.strftime("%d/%m/%Y - %H:%M"))
        return self.date.strftime("%d/%m/%Y - %H:%M")

    @property
    def total(self):
        items = Item.objects.filter(sell_id=self.id).select_related("product").annotate(total_price=models.Sum('product__price'))
        total = 0
        for item in items:
            total += item.total_price * item.quantity
        return round(total, 2)

    @property
    def total_items(self):
        items = Item.objects.filter(sell_id=self.id)
        total = 0
        for item in items:
            total += item.quantity
        return total

    @property
    def total_commission(self):
        items = Item.objects.filter(sell_id=self.id)
        total = 0
        for item in items:
            total += item.commission_amount
        return round(total, 2)

    @property
    def items(self):
        items = Item.objects.filter(sell_id=self.id).select_related("product")
        return items


class Item(models.Model):
    sell = models.ForeignKey("Sell", on_delete=models.CASCADE, related_name="sell")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('sell', 'product'), name='once_per_product_sale')
        ]

    @property
    def total(self):
        return self.quantity * self.product.price

    @property
    def commission_amount(self):
        return round(self.quantity * self.product.price * self.product.commission / 100, 2)

    def __str__(self):
        return self.product.description


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

