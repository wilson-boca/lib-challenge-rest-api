from django.contrib.auth.models import User, Group
from store.models import Item, Client, Seller, Product, Sell
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['name', 'email', 'phone']


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'code', 'description', 'price', 'commission']


class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sell
        fields = ['invoice', 'date_fmt', 'client', 'seller']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemsSerializer(serializers.ModelSerializer):

    product_service = serializers.SerializerMethodField()

    def get_product_service(self, obj):
        return f"{obj.product.code} - {obj.product.description}"

    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return obj.product.price

    commission = serializers.SerializerMethodField()

    def get_commission(self, obj):
        return obj.product.commission

    class Meta:
        model = Item
        fields = ['product_service', 'quantity', 'price', 'total', 'commission','commission_amount']


class SalesSerializer(serializers.HyperlinkedModelSerializer):

    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        return ItemsSerializer(obj.items, many=True).data

    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        return obj.total

    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        return obj.total

    class Meta:
        model = Sell
        fields = ['id', 'invoice', 'client_name', 'seller_name', 'date_fmt', 'total', 'items', 'total_items', 'total_commission']
