# Generated by Django 4.1.3 on 2022-12-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='santa-claus-g93042808a_640.png', null=True, upload_to='./static/product_images'),
        ),
    ]
