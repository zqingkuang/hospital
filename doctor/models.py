from django.db import models
from user.models import *
from tinymce.models import HTMLField


class Doctor(models.Model):
    """医生模型类"""
    EDUCATION_TYPE_CHOICES = (
        (1, '大专'),
        (2, '本科'),
        (3, '硕士'),
        (4, '博士')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name='用户id')
    ID_number = models.CharField(max_length=18, verbose_name='身份证号')
    cell_phone = models.IntegerField(verbose_name='手机号')
    sex = models.SmallIntegerField(choices=((0, '女'), (1, '男')), verbose_name='性别')
    age = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='科室')
    education = models.SmallIntegerField(choices=EDUCATION_TYPE_CHOICES, verbose_name='学历')
    remarks = HTMLField(blank=True, verbose_name='备注信息')
    time = models.DateTimeField(auto_now_add=True, verbose_name='入职时间')