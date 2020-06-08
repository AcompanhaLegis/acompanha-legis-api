from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(blank=False, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
