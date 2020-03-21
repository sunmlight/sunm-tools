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


class TaskInfo(models.Model):
    task_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    run_type = models.IntegerField(default=0, choices=())
    status = models.IntegerField(default=0)
    result = models.CharField(max_length=50, blank=True, null=True)
    script = models.TextField(blank=True, null=True, verbose_name="脚本")
    count = models.IntegerField(default=0, verbose_name="总计")
    last_run_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "TaskInfo"
        verbose_name_plural = "TaskInfo"

    def __str__(self):
        return self.name