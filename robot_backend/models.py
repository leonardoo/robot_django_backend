# -*- coding: utf-8 -*-

import uuid

from django.conf import settings
from django.db import models


class UserSecretModel(models.Model):

    secret_key = models.CharField(max_length=50, default=uuid.uuid4, editable=False)
    public_key = models.CharField(max_length=50, default=uuid.uuid4, editable=False) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        unique_together = ("user", "secret_key", "public_key")
        verbose_name = "UserSecret"
        verbose_name_plural = "UserSecrets"
