from django.db import models
from user.models import *
from doctor.models import *


class Registration(models.Model):
    """挂号信息模型类"""
    SELF_PAYING = (
        (1, '自费'),
        (2, '不自费')
    )
    EXAMINATION_STATUS = (
        (1, '初诊'),
        (2, '复诊')
    )
    REGISTRATION_STATUS = (
        (1, '已挂号'),
        (2, '已住院'),
        (3, '已退号')
    )
    r_name = models.CharField(max_length=20, verbose_name='姓名')
    r_ID_number = models.CharField(max_length=18, verbose_name='身份证号')
    r_social_security = models.CharField(max_length=12, verbose_name='社保号')
    r_registration_fee = models.IntegerField(verbose_name='挂号费')
    r_phone = models.CharField(max_length=11, verbose_name='电话号')
    r_self_paying = models.SmallIntegerField(choices=SELF_PAYING, verbose_name='是否自费')
    r_sex = models.CharField(max_length=2, verbose_name='性别')
    r_age = models.IntegerField(verbose_name='年龄')
    r_profession = models.CharField(max_length=50, verbose_name='职业')
    r_examination = models.SmallIntegerField(choices=EXAMINATION_STATUS, verbose_name='初复诊')
    r_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='所挂科室')
    r_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='所挂医生')
    r_remarks = models.CharField(max_length=100, verbose_name='备注')
    r_time = models.DateTimeField(auto_now_add=True, verbose_name='挂号时间')
    r_status = models.SmallIntegerField(choices=REGISTRATION_STATUS, default=1, verbose_name='挂号状态')


class Hospital(models.Model):
    """住院模型类"""
    HOSPITAL_STATUS = (
        (1, '已住院'),
        (2, '已出院'),
        (3, '已结算')
    )
    h_registration = models.ForeignKey(Registration, on_delete=models.CASCADE, verbose_name='挂号表信息')
    h_nurse = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='护理人员信息')
    h_BedID = models.CharField(max_length=10, verbose_name='床位号')
    h_cash_pledge = models.IntegerField(verbose_name='缴费押金')
    h_disease = models.CharField(max_length=150, verbose_name='病情')
    h_status = models.SmallIntegerField(choices=HOSPITAL_STATUS, verbose_name='住院状态')
    h_time = models.DateTimeField(auto_now_add=True, verbose_name='入院时间')


class Cost(models.Model):
    """费用模型类"""
    c_registration = models.ForeignKey(Registration, on_delete=models.CASCADE, verbose_name='挂号信息')
    c_name = models.CharField(max_length=100, verbose_name='费用名称')
    c_price = models.IntegerField(verbose_name='费用价格')
    c_time = models.DateTimeField(auto_now_add=True)


