from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    full_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    # add additional fields in here

    def __str__(self):
        return self.username
