# Generated by Django 2.1.3 on 2019-07-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20190716_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='d_status',
            field=models.SmallIntegerField(choices=[(1, '在售'), (2, '停售')], default=1, verbose_name='药品状态'),
        ),
    ]