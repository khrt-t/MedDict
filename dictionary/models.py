from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class DjangoGroup:
    pass


class Group(DjangoGroup):
    class Meta:
        proxy = True


class CustomUser(AbstractUser):
    pass
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
