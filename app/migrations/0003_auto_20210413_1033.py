# Generated by Django 3.2 on 2021-04-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210413_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='total',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='multiple',
            field=models.PositiveIntegerField(default=1, verbose_name='multiplo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='preço'),
        ),
    ]