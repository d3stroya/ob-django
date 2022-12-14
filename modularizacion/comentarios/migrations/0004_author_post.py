# Generated by Django 4.1.3 on 2022-12-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comments_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20, null=True)),
                ('alias', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(default='Hey there!', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=10000)),
            ],
        ),
    ]
