from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    auth = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    wechat = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = "UserInfo"

    def __str__(self):
        return self.username
