# Generated by Django 2.1.3 on 2019-07-10 08:15

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_number', models.CharField(max_length=18, verbose_name='身份证号')),
                ('cell_phone', models.IntegerField(verbose_name='手机号')),
                ('sex', models.SmallIntegerField(choices=[(0, '女'), (1, '男')], verbose_name='性别')),
                ('age', models.IntegerField()),
                ('education', models.SmallIntegerField(choices=[(1, '大专'), (2, '本科'), (3, '硕士'), (4, '博士')], verbose_name='学历')),
                ('remarks', tinymce.models.HTMLField(blank=True, verbose_name='备注信息')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='入职时间')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Section', verbose_name='科室')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户id')),
            ],
        ),
    ]