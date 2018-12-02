<<<<<<< HEAD
from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
=======
from django.db import models

# Create your models here.
>>>>>>> 4a479e64b193376f83d147cd6b36d3adf5978e66
