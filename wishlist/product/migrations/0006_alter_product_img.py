# Generated by Django 4.1.3 on 2022-12-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='https://cdn.pixabay.com/photo/2017/11/07/19/23/santa-claus-2927962_960_720.png', null=True, upload_to='static/product_images'),
        ),
    ]