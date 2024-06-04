from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_("E-mail"))
    profile_img = models.ImageField(upload_to="users/profile/images/", blank=True, verbose_name=_("User Profile Image"))