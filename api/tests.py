import pytest
import json

from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_get_sell_success(new_sell, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get('/api/sell/')
    assert result.data[0].get("invoice") == new_sell.invoice
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_sell_not_authorized(new_sell):
    client.credentials(HTTP_AUTHORIZATION='Token any_fake_token')
    result = client.get('/api/sell/')
    assert result.data.get("detail") == "Invalid token."
    assert result.status_code == 401


@pytest.mark.django_db
def test_get_sell_success_with_id(new_sell, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get(f'/api/sell/{new_sell.id}/')
    assert result.data.get("invoice") == new_sell.invoice
    assert result.status_code == 200


@pytest.mark.django_db
def test_city_post_method(new_sell, sell_put, new_client, get_token, seller):
    data = json.dumps(sell_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.post(f'/api/sell/', data, content_type='application/json')
    assert response.data.get("client") == 2
    assert response.status_code == 201


@pytest.mark.django_db
def test_city_put_method(new_sell, sell_put, get_token, new_client, seller):
    data = json.dumps(sell_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.put(f'/api/sell/{new_sell.id}/', data, content_type='application/json')
    assert response.data.get('client') == new_client.id
    assert response.status_code == 200


@pytest.mark.django_db
def test_city_delete_method(new_sell, get_token, seller):
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.delete(f'/api/sell/{new_sell.id}/')
    assert response.status_code == 204
