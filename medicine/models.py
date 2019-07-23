from django.db import models
from registration.models import *


class Drug(models.Model):
    """药品模型类"""
    DRUG_TYPE = (
        (1, '处方药'),
        (2, '非处方药'),
        (3, '中药')
    )
    DRUG_STATUS = (
        (1, '在售'),
        (2, '停售')
    )
    d_picture = models.ImageField(upload_to='medicine', verbose_name='药品图片')
    d_number = models.CharField(max_length=11, verbose_name='药品编号')
    d_p_price = models.IntegerField(verbose_name='药品进价')
    d_s_price = models.IntegerField(verbose_name='药品售价')
    d_name = models.CharField(max_length=50, verbose_name='药品名称')
    d_type = models.SmallIntegerField(choices=DRUG_TYPE, verbose_name='药品类型')
    d_describe = models.CharField(max_length=500, verbose_name='药品简述描述')
    d_expiration_date = models.CharField(max_length=5, verbose_name='保质期')
    d_detail = models.TextField(verbose_name='药品详细描述')
    d_manufacturers = models.CharField(max_length=100, verbose_name='生产厂家')
    d_explain = models.TextField(verbose_name='药品说明')
    d_remarks = models.CharField(max_length=1000, verbose_name='备注')
    d_inventory = models.IntegerField(verbose_name='药品库存')
    d_status = models.SmallIntegerField(choices=DRUG_STATUS, verbose_name='药品状态', default=1)
    def status(self):
        if self.d_status == 1:
            return '在售'
        elif self.d_status == 2:
            return '停售'

    def type(self):
        if self.d_type == 1:
            return '处方药'
        elif self.d_type == 2:
            return '非处方药'
        elif self.d_type == 3:
            return '中药'


class Pharmacy(models.Model):
    """用药模型类"""
    p_registration = models.ForeignKey(Registration, on_delete=models.CASCADE, verbose_name='挂号信息')
    p_drug = models.ForeignKey(Drug, on_delete=models.CASCADE, verbose_name='药品信息')
    p_number = models.IntegerField(verbose_name='用药数量')
    s_number = models.IntegerField(verbose_name='已发数量')
    d_number = models.IntegerField(verbose_name='未发数量')
