from django.db import models

# Create your models here.


class Role(models.Model):
    """角色模型类"""
    r_name = models.CharField(max_length=10, verbose_name='角色名称')


class Jurisdiction(models.Model):
    """权限模型类"""
    j_name = models.CharField(max_length=30, verbose_name='权限名称')
    models.ManyToManyField(Role)


class Section(models.Model):
    """科室模型类"""
    name = models.CharField(max_length=5, verbose_name='科室名称')


class User(models.Model):
    """用户模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用')
    )
    user = models.CharField(max_length=20, verbose_name='账户')
    password = models.CharField(max_length=20, verbose_name='密码')
    name = models.CharField(max_length=20, verbose_name='姓名')
    email = models.EmailField(blank=False, verbose_name='电子邮箱')
    status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=0, verbose_name='状态')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='角色用户')
    time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')




