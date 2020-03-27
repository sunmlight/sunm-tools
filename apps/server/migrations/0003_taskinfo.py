# Generated by Django 3.0.4 on 2020-03-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20200320_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('run_type', models.IntegerField(choices=[(0, '按延迟时间执行'), (1, '按指定日期执行')], default=0)),
                ('status', models.IntegerField(default=0)),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField(default=0, verbose_name='执行次数')),
                ('last_run_time', models.DateTimeField(blank=True, null=True)),
                ('last_run_status', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=False)),
                ('script', models.TextField(blank=True, null=True, verbose_name='脚本')),
            ],
            options={
                'verbose_name': 'TaskInfo',
                'verbose_name_plural': 'TaskInfo',
            },
        ),
    ]