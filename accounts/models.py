from django.contrib.auth.models import AbstractUser
from django.db import models


ROLES = (
    ('regular', 'Regular'),
    ('agent', 'Agent'),
    ('admin', 'Admin'),
)


class User(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLES, default='regular')
