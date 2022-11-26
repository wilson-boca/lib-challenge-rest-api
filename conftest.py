import pytest

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from model_bakery import baker


@pytest.fixture
def new_sell(db):
    return baker.make('store.Sell')


@pytest.fixture
def new_seller(db):
   return baker.make('store.Seller')


@pytest.fixture
def new_client(db):
    return baker.make('store.Client')


@pytest.fixture
def new_product(db):
    return baker.make('store.Product')


@pytest.fixture
def new_item(db):
    return baker.make('store.Item')


@pytest.fixture
def seller(db):
    return baker.make('store.Seller')


@pytest.fixture
@pytest.mark.django_db
def get_token(db):
    user = User.objects.create(
        username="admin",
        password="admin321",
        email="admin@provider.com",
        first_name="test first name",
        last_name="test last name",
        is_superuser=True,
        is_staff=True,
        is_active=True
    )
    token = Token.objects.create(user=user)
    return token.key


@pytest.fixture
def sell_put(db):
    return {
        "client": 2,
        "seller": 1
    }


@pytest.fixture
def seller_put(db):
    return {
        "name": "Tester Name",
        "email": "test@provider.com",
        "phone": "11222333445"
    }


@pytest.fixture
def client_put(db):
    return {
        "name": "New Client Name",
        "email": "newc@provider.com",
        "phone": "19777777777"
    }


@pytest.fixture
def product_put(db):
    return {
        "code": "00002",
        "description": "New Product Name",
        "price": 5,
        "commission": 2
    }
