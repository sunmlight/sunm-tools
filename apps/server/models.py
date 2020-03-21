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
    run_type_choices = (
        (0, "按延迟时间执行"),  # case: 10s 后执行
        (1, "按指定日期执行"),  # case: 2020-10-1 执行
    )
    task_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    run_type = models.IntegerField(default=0, choices=run_type_choices)
    status = models.IntegerField(default=0)
    result = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(default=0, verbose_name="执行次数")  # 0：已执行完不再执行  -1：无限次执行
    last_run_time = models.DateTimeField(blank=True, null=True)
    last_run_status = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    script = models.TextField(blank=True, null=True, verbose_name="脚本")  # 暂时只执行代项目内脚本

    class Meta:
        verbose_name = "TaskInfo"
        verbose_name_plural = "TaskInfo"

    def __str__(self):
        return self.name
