import pytest

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from model_bakery import baker


@pytest.fixture
def new_sell(db):
    return baker.make('store.Sell')


@pytest.fixture
def new_client(db):
    return baker.make('store.Client')


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
