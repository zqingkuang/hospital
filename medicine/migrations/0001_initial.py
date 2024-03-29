# Generated by Django 2.1.3 on 2019-07-10 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_picture', models.ImageField(upload_to='medicine', verbose_name='药品图片')),
                ('d_p_price', models.IntegerField(verbose_name='药品进价')),
                ('d_s_price', models.IntegerField(verbose_name='药品售价')),
                ('d_name', models.CharField(max_length=50, verbose_name='药品名称')),
                ('d_type', models.SmallIntegerField(choices=[(1, '处方药'), (2, '非处方药'), (3, '中药')], verbose_name='药品类型')),
                ('d_describe', models.CharField(max_length=100, verbose_name='药品简述描述')),
                ('d_expiration_date', models.CharField(max_length=5, verbose_name='保质期')),
                ('d_detail', models.TextField(verbose_name='药品详细描述')),
                ('d_manufacturers', models.CharField(max_length=100, verbose_name='生产厂家')),
                ('d_explain', models.TextField(verbose_name='药品说明')),
                ('d_remarks', models.CharField(max_length=100, verbose_name='备注')),
                ('d_inventory', models.IntegerField(verbose_name='药品库存')),
                ('d_status', models.SmallIntegerField(choices=[(1, '在售'), (2, '停售')], verbose_name='药品状态')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_number', models.IntegerField(verbose_name='用药数量')),
                ('s_number', models.IntegerField(verbose_name='已发数量')),
                ('d_number', models.IntegerField(verbose_name='未发数量')),
                ('p_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Drug', verbose_name='药品信息')),
                ('p_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Registration', verbose_name='挂号信息')),
            ],
        ),
    ]
