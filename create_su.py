from django.db import IntegrityError
from django.contrib.auth.models import User


try:
    superuser = User.objects.create_superuser(
        username="admin",
        email="admin@provider.com",
        password="admin321")
    superuser.save()
    print("Super user has been created, check the README.md for the user and password")
except IntegrityError:
    print("Everything is okay, this user already exist, check the README.md for the user and password")
except Exception as e:
    print(str(e))
