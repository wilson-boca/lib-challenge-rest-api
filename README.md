# lib-challenge-rest-api
Django REST API - Library Challenge

## Environment:
- Python version: 3.11
- Django REST framework version: 3.11.0

## Super User Login
- The credentials for the admin login are:
```
user: admin
password: admin321
```

## Testing

To run the project on a Docker container execute the command below on the root folder.
It will load everything that the application needs(PostgreSQL, PGAdmin)
```
$export USE_TEST_DB=true
$pytest --cov --cov-report=html
```

## Running

To run the project on a Docker container execute the command below on the root folder.
It will load everything that the application needs(PostgreSQL, PGAdmin)
```
$export DB_HOST=localhost
$docker-compose up -d
```

Now you are able to access the APP on PORT 8000:

[http://localhost:8000](http://localhost:8000)

## URLs:
-    [http://localhost:8000/admin](http://localhost:8000)
-    [http://localhost:8000/api](http://localhost:8000)
