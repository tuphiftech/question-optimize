import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from safedelete.models import SafeDeleteMixin

class User(SafeDeleteMixin, AbstractBaseUser):
    USERNAME_FIELD = "username"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=150, unique=True, blank=True, null=True
    )