from django.contrib.auth.models import User, Group
from store.models import Sell, Item
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemsSerializer(serializers.HyperlinkedModelSerializer):

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


class SellsSerializer(serializers.HyperlinkedModelSerializer):

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
        fields = ['fiscal_code', 'client_name', 'seller_name', 'date_fmt', 'total', 'items', 'total_items', 'total_commission']
