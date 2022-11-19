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

