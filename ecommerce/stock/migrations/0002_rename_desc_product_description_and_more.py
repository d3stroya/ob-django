# Generated by Django 4.1.3 on 2022-12-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='short_desc',
            new_name='short_description',
        ),
    ]
