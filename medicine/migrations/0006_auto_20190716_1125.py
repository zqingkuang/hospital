# Generated by Django 2.1.3 on 2019-07-16 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_auto_20190716_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='d_inventory',
            field=models.IntegerField(default=2000, verbose_name='药品库存'),
        ),
    ]