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


# seller
@pytest.mark.django_db
def test_get_seller_success(new_seller, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get('/api/seller/')
    assert result.data[0].get("name") == new_seller.name
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_seller_not_authorized(new_seller):
    client.credentials(HTTP_AUTHORIZATION='Token any_fake_token')
    result = client.get('/api/seller/')
    assert result.data.get("detail") == "Invalid token."
    assert result.status_code == 401


@pytest.mark.django_db
def test_get_seller_success_with_id(new_seller, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get(f'/api/seller/{new_seller.id}/')
    assert result.data.get("name") == new_seller.name
    assert result.status_code == 200


@pytest.mark.django_db
def test_seller_post_method(new_seller, seller_put, get_token, seller):
    data = json.dumps(seller_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.post(f'/api/seller/', data, content_type='application/json')
    assert response.data.get("name") == seller_put.get("name")
    assert response.status_code == 201


@pytest.mark.django_db
def test_seller_put_method(new_seller, seller_put, get_token, seller):
    seller_put['name'] = "New name"
    data = json.dumps(seller_put)

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.put(f'/api/seller/{new_seller.id}/', data, content_type='application/json')
    assert response.data.get('name') == 'New name'
    assert response.status_code == 200


@pytest.mark.django_db
def test_seller_delete_method(new_seller, get_token):
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.delete(f'/api/seller/{new_seller.id}/')
    assert response.status_code == 204


# client
@pytest.mark.django_db
def test_get_client_success(new_client, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get('/api/client/')
    assert result.data[0].get("name") == new_client.name
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_client_not_authorized(new_client):
    client.credentials(HTTP_AUTHORIZATION='Token any_fake_token')
    result = client.get('/api/client/')
    assert result.data.get("detail") == "Invalid token."
    assert result.status_code == 401


@pytest.mark.django_db
def test_get_client_success_with_id(new_client, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get(f'/api/client/{new_client.id}/')
    assert result.data.get("name") == new_client.name
    assert result.status_code == 200


@pytest.mark.django_db
def test_client_post_method(client_put, get_token, seller):
    data = json.dumps(client_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.post(f'/api/client/', data, content_type='application/json')
    assert response.data.get("name") == client_put.get("name")
    assert response.status_code == 201


@pytest.mark.django_db
def test_client_put_method(new_client, client_put, get_token, seller):
    client_put['name'] = "New Client Name 2"
    data = json.dumps(client_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.put(f'/api/client/{new_client.id}/', data, content_type='application/json')
    assert response.data.get('name') == 'New Client Name 2'
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_delete_method(new_client, get_token):
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.delete(f'/api/client/{new_client.id}/')
    assert response.status_code == 204


# product
@pytest.mark.django_db
def test_get_product_success(new_product, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get('/api/product/')
    assert result.data[0].get("description") == new_product.description
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_product_not_authorized(new_client):
    client.credentials(HTTP_AUTHORIZATION='Token any_fake_token')
    result = client.get('/api/product/')
    assert result.data.get("detail") == "Invalid token."
    assert result.status_code == 401


@pytest.mark.django_db
def test_get_product_success_with_id(new_product, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get(f'/api/product/{new_product.id}/')
    assert result.data.get("description") == new_product.description
    assert result.status_code == 200


@pytest.mark.django_db
def test_product_post_method(product_put, get_token):
    data = json.dumps(product_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.post(f'/api/product/', data, content_type='application/json')
    assert response.data.get("description") == product_put.get("description")
    assert response.status_code == 201


@pytest.mark.django_db
def test_product_put_method(new_product, product_put, get_token):
    product_put['description'] = "New Product Name 2"
    data = json.dumps(product_put)
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.put(f'/api/product/{new_product.id}/', data, content_type='application/json')
    assert response.data.get('description') == 'New Product Name 2'
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_delete_method(new_product, get_token):
    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    response = client.delete(f'/api/product/{new_product.id}/')
    assert response.status_code == 204


# sales
@pytest.mark.django_db
def test_get_sales_success(new_sell, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get('/api/sales/')
    assert result.data[0].get("invoice") == new_sell.invoice
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_sales_not_authorized(new_client):
    client.credentials(HTTP_AUTHORIZATION='Token any_fake_token')
    result = client.get('/api/sales/')
    assert result.data.get("detail") == "Invalid token."
    assert result.status_code == 401


@pytest.mark.django_db
def test_get_sales_success_with_id(new_sell, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get(f'/api/sales/{new_sell.id}/')
    assert result.data.get("total_items") == new_sell.total_items
    assert result.status_code == 200


# commission
@pytest.mark.django_db
def test_get_commission_success(new_sell, get_token):

    client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    result = client.get('/api/commission/')
    result_dict = json.loads(result.content.decode())
    assert result_dict.get('data')[0].get('total_items') == 0
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_sales_not_authorized(new_client):
    client.credentials(HTTP_AUTHORIZATION='Token any_fake_token')
    result = client.get('/api/commission/')
    assert result.data.get("detail") == "Invalid token."
    assert result.status_code == 401
