from store.models import Item, Product, Sell, Seller, Client


def create_products_for_sell(products: list[dict]) -> dict:
    products_list = products.get("product")
    seller = Seller.objects.get(id=products.get("seller"))
    client = Client.objects.get(id=products.get("client"))
    sell = Sell.objects.create(seller=seller, client=client)

    for product in products_list:
        product_instance = Product.objects.get(id=product.get("id"))
        Item.objects.create(product=product_instance, sell=sell, quantity=product.get("quantity"))

    return sell


def group_by(start_date, end_date):
    result = []
    for seller in Seller.objects.all().order_by('id'):
        total_comission = 0
        total_items = 0
        for sell in Sell.objects.filter(seller=seller, date__range=[start_date, end_date]):
            total_comission += sell.total_commission
            total_items += sell.total_items
        result_dict = {
            "id": str(seller.id).zfill(3),
            "name": seller.name,
            "total_items": total_items,
            "total_commission": total_comission
        }
        result.append(result_dict)
    return result
